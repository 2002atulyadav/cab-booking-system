from typing import Dict, List, Optional
from models.booking import Ride, RideStatus
from models.location import Location
from models.user import User
from models.driver import Driver


class RideService:
    RATE_PER_UNIT = 1.0  # $1 per unit distance
    
    def __init__(self):
        self._active_rides: Dict[str, Ride] = {}  # username -> Ride
        self._pending_searches: Dict[str, dict] = {}  # username -> {source, destination, available_drivers}
    
    def store_ride_search(self, username: str, source: Location, destination: Location, 
                          available_drivers: List[Driver]) -> None:
        """Store the ride search results for a user"""
        self._pending_searches[username] = {
            'source': source,
            'destination': destination,
            'available_drivers': [d.name for d in available_drivers]
        }
    
    def get_pending_search(self, username: str) -> Optional[dict]:
        """Get pending search for a user"""
        return self._pending_searches.get(username)
    
    def create_ride(self, user: User, driver: Driver, source: Location, 
                    destination: Location) -> Ride:
        """Create a new ride"""
        ride = Ride(
            user=user,
            driver=driver,
            source=source,
            destination=destination,
            status=RideStatus.IN_PROGRESS
        )
        self._active_rides[user.username] = ride
        
        # Clear pending search
        if user.username in self._pending_searches:
            del self._pending_searches[user.username]
        
        return ride
    
    def get_active_ride(self, username: str) -> Optional[Ride]:
        """Get active ride for a user"""
        return self._active_rides.get(username)
    
    def complete_ride(self, username: str) -> Optional[Ride]:
        """Complete a ride and calculate bill"""
        ride = self._active_rides.get(username)
        if not ride:
            return None
        
        ride.status = RideStatus.COMPLETED
        distance = ride.calculate_distance()
        ride.bill_amount = round(distance * self.RATE_PER_UNIT)
        
        # Remove from active rides
        del self._active_rides[username]
        
        return ride
    
    def has_active_ride(self, username: str) -> bool:
        """Check if user has an active ride"""
        return username in self._active_rides