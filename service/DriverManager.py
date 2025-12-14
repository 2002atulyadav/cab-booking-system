from typing import Dict, List, Optional
from models.driver import Driver
from models.vehicle import Vehicle
from models.location import Location


class DriverService:
    MAX_PICKUP_DISTANCE = 5.0
    
    def __init__(self):
        self._drivers: Dict[str, Driver] = {}
    
    def add_driver(self, driver_details: str, vehicle_details: str, location: tuple) -> str:
        """
        Add a new driver.
        driver_details: 'name, gender, age'
        vehicle_details: 'model, registration_number'
        location: (x, y)
        """
        try:
            # Parse driver details
            d_parts = [p.strip() for p in driver_details.split(',')]
            if len(d_parts) != 3:
                raise ValueError("Invalid driver details format")
            name, gender, age = d_parts
            
            if name in self._drivers:
                raise ValueError(f"Driver {name} already exists")
            
            # Parse vehicle details
            v_parts = [p.strip() for p in vehicle_details.split(',')]
            if len(v_parts) != 2:
                raise ValueError("Invalid vehicle details format")
            model, reg_number = v_parts
            
            vehicle = Vehicle(model=model, registration_number=reg_number)
            driver_location = Location(x=location[0], y=location[1])
            
            driver = Driver(
                name=name,
                gender=gender,
                age=int(age),
                vehicle=vehicle,
                current_location=driver_location,
                is_available=True,
                total_earnings=0.0
            )
            
            self._drivers[name] = driver
            return f"Driver {name} added successfully"
        except Exception as e:
            raise Exception(f"Failed to add driver: {str(e)}")
    
    def update_driver_location(self, driver_name: str, location: tuple) -> str:
        """Update driver's current location"""
        if driver_name not in self._drivers:
            raise ValueError(f"Driver {driver_name} not found")
        
        self._drivers[driver_name].current_location = Location(x=location[0], y=location[1])
        return f"Driver {driver_name} location updated to {location}"
    
    def change_driver_status(self, driver_name: str, is_available: bool) -> str:
        """Change driver's availability status"""
        if driver_name not in self._drivers:
            raise ValueError(f"Driver {driver_name} not found")
        
        self._drivers[driver_name].is_available = is_available
        status = "available" if is_available else "unavailable"
        return f"Driver {driver_name} is now {status}"
    
    def find_available_drivers(self, user_location: Location) -> List[Driver]:
        """Find all available drivers within MAX_PICKUP_DISTANCE"""
        available_drivers = []
        
        for driver in self._drivers.values():
            if not driver.is_available:
                continue
            
            distance = user_location.distance_to(driver.current_location)
            if distance <= self.MAX_PICKUP_DISTANCE:
                available_drivers.append(driver)
        
        # Sort by distance (nearest first)
        available_drivers.sort(
            key=lambda d: user_location.distance_to(d.current_location)
        )
        
        return available_drivers
    
    def get_driver(self, driver_name: str) -> Optional[Driver]:
        """Get driver by name"""
        return self._drivers.get(driver_name)
    
    def add_earnings(self, driver_name: str, amount: float) -> None:
        """Add earnings to driver"""
        if driver_name in self._drivers:
            self._drivers[driver_name].total_earnings += amount
    
    def get_all_drivers(self) -> Dict[str, Driver]:
        """Get all drivers"""
        return self._drivers