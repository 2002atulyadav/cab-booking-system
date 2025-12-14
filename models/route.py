from dataclasses import dataclass
from models.location import Location
from models.driver import Driver

@dataclass
class StopingPoint:
    stop_point : Location
    arrival_time : str
    wait_time : str


@dataclass
class Route:
    route_id : int
    source : Location
    destination : Location
    start_time : str
    end_time : str
    stoping_point : {StopingPoint}
    driver : Driver


