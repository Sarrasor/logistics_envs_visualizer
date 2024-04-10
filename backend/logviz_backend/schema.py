from enum import Enum
from typing import Optional

from pydantic import BaseModel


class HealthcheckStatus(str, Enum):
    DOWN = "DOWN"
    UP = "UP"


class Healthcheck(BaseModel):
    status: HealthcheckStatus


class Location(BaseModel):
    lat: float
    lon: float


class WorkerStatus(str, Enum):
    IDLE = "IDLE"
    MOVING = "MOVING"
    MOVING_TO_PICKUP = "MOVING_TO_PICKUP"
    MOVING_TO_DROP_OFF = "MOVING_TO_DROP_OFF"
    PICKING_UP = "PICKING_UP"
    DROPPING_OFF = "DROPPING_OFF"


class WorkerTravelType(str, Enum):
    WALK = "WALK"
    BIKE = "BIKE"
    CAR = "CAR"


class WorkerObservation(BaseModel):
    id: str
    location: Location
    travel_type: WorkerTravelType
    speed: float
    path: Optional[str]
    remaining_path_index: Optional[int]
    status: WorkerStatus
    color: str


class OrderStatus(str, Enum):
    CREATED = "CREATED"
    IN_PICKUP = "IN_PICKUP"
    IN_DELIVERY = "IN_DELIVERY"
    IN_DROP_OFF = "IN_DROP_OFF"
    COMPLETED = "COMPLETED"


class OrderObservation(BaseModel):
    id: str
    client_id: str
    from_location: Location
    to_location: Location
    creation_time: int
    time_window: list[tuple[int, int]]
    status: OrderStatus


class Bounds(BaseModel):
    min: Location
    max: Location


class Observation(BaseModel):
    current_time: int
    bounds: Bounds
    workers: list[WorkerObservation]
    orders: list[OrderObservation]


class Info(BaseModel):
    simulation_id: str
    start_time: int
    end_time: int


class RenderRequest(BaseModel):
    observation: Observation
    info: Info


class RenderStatus(str, Enum):
    OK = "OK"
    ERROR = "ERROR"


class RenderResponse(BaseModel):
    status: RenderStatus
