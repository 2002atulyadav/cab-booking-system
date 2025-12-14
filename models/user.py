from dataclasses import dataclass
from typing import Optional
from models.location import Location


@dataclass
class User:
    username: str
    gender: str
    age: int
    current_location: Optional[Location] = None
    