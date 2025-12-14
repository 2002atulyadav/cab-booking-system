from enum import Enum

class BookingStatus(Enum):
    REQUESTED = "requested"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    CANCELLED = "cancelled"

class VehicleType(Enum):
    AUTORICKSHAW = "autorickshaw"
    MINI = "mini"
    SEDAN = "sedan"
    SUV = "suv"
    XL = "xl"

