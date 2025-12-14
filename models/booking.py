from dataclasses import dataclass
from enum import Enum
from models.location import Location
from models.user import User
from models.driver import Driver


class RideStatus(Enum):
    REQUESTED = "requested"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    CANCELLED = "cancelled"


@dataclass
class Ride:
    user: User
    driver: Driver
    source: Location
    destination: Location
    status: RideStatus = RideStatus.REQUESTED
    bill_amount: float = 0.0
    
    def calculate_distance(self) -> float:
        """Calculate distance between source and destination"""
        return self.source.distance_to(self.destination)