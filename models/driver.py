from dataclasses import dataclass, field
from typing import Optional
from models.location import Location
from models.vehicle import Vehicle


@dataclass
class Driver:
    name: str
    gender: str
    age: int
    vehicle: Vehicle
    current_location: Location
    is_available: bool = True
    total_earnings: float = 0.0