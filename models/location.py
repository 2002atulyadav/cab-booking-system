from dataclasses import dataclass
import math


@dataclass
class Location:
    x: float
    y: float
    
    def distance_to(self, other: 'Location') -> float:
        """Calculate Euclidean distance to another location"""
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)