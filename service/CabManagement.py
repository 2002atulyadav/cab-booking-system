from typing import List, Dict
from models.location import Location
from service.UserManagement import UserService
from service.DriverManager import DriverService
from service.RouteManagement import RideService


class CabBookingService:
    """Main service that orchestrates all cab booking operations"""
    
    def __init__(self):
        self._user_service = UserService()
        self._driver_service = DriverService()
        self._ride_service = RideService()
    
    # User Operations
    def add_user(self, user_details: str) -> str:
        return self._user_service.add_user(user_details)
    
    def update_user(self, username: str, updated_details: str) -> str:
        return self._user_service.update_user(username, updated_details)
    
    def update_user_location(self, username: str, location: tuple) -> str:
        return self._user_service.update_user_location(username, location)
    
    # Driver Operations
    def add_driver(self, driver_details: str, vehicle_details: str, location: tuple) -> str:
        return self._driver_service.add_driver(driver_details, vehicle_details, location)
    
    def update_driver_location(self, driver_name: str, location: tuple) -> str:
        return self._driver_service.update_driver_location(driver_name, location)
    
    def change_driver_status(self, driver_name: str, is_available: bool) -> str:
        return self._driver_service.change_driver_status(driver_name, is_available)
    
    # Ride Operations
    def find_ride(self, username: str, source: tuple, destination: tuple) -> str:
        """Find available rides for a user"""
        user = self._user_service.get_user(username)
        if not user:
            raise ValueError(f"User {username} not found")
        
        if self._ride_service.has_active_ride(username):
            raise ValueError(f"User {username} already has an active ride")
        
        source_location = Location(x=source[0], y=source[1])
        destination_location = Location(x=destination[0], y=destination[1])
        
        # Update user location to source
        self._user_service.update_user_location(username, source)
        
        # Find available drivers
        available_drivers = self._driver_service.find_available_drivers(source_location)
        
        if not available_drivers:
            return "No ride found"
        
        # Store search results for later selection
        self._ride_service.store_ride_search(
            username, source_location, destination_location, available_drivers
        )
        
        # Return available drivers
        driver_list = ", ".join([f"{d.name} [Available]" for d in available_drivers])
        return driver_list
    
    def choose_ride(self, username: str, driver_name: str) -> str:
        """Choose a specific driver for the ride"""
        user = self._user_service.get_user(username)
        if not user:
            raise ValueError(f"User {username} not found")
        
        driver = self._driver_service.get_driver(driver_name)
        if not driver:
            raise ValueError(f"Driver {driver_name} not found")
        
        if not driver.is_available:
            raise ValueError(f"Driver {driver_name} is not available")
        
        # Get pending search
        pending = self._ride_service.get_pending_search(username)
        if not pending:
            raise ValueError(f"No ride search found for user {username}. Please search for a ride first.")
        
        if driver_name not in pending['available_drivers']:
            raise ValueError(f"Driver {driver_name} was not in the available drivers list")
        
        # Create ride
        ride = self._ride_service.create_ride(
            user=user,
            driver=driver,
            source=pending['source'],
            destination=pending['destination']
        )
        
        # Mark driver as unavailable
        self._driver_service.change_driver_status(driver_name, False)
        
        return "Ride Started"
    
    def calculate_bill(self, username: str) -> str:
        """Calculate and return bill for completed ride"""
        ride = self._ride_service.complete_ride(username)
        if not ride:
            raise ValueError(f"No active ride found for user {username}")
        
        # Update locations
        dest = ride.destination
        self._user_service.update_user_location(username, (dest.x, dest.y))
        self._driver_service.update_driver_location(ride.driver.name, (dest.x, dest.y))
        
        # Add earnings to driver
        self._driver_service.add_earnings(ride.driver.name, ride.bill_amount)
        
        # Driver becomes available again after ride
        self._driver_service.change_driver_status(ride.driver.name, True)
        
        return f"Ride Ended bill amount ${int(ride.bill_amount)}"
    
    def find_total_earning(self) -> str:
        """Get total earnings of all drivers"""
        drivers = self._driver_service.get_all_drivers()
        result = []
        
        for name, driver in drivers.items():
            result.append(f"{name} earned ${int(driver.total_earnings)}")
        
        return "\n".join(result)
