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
    IN_SERVICE = "IN_SERVICE"
    MOVING = "MOVING"
    MOVING_TO_SERVICE = "MOVING_TO_SERVICE"
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
    fuel: float
    path: Optional[str]
    remaining_path_index: Optional[int]
    status: WorkerStatus
    color: str


class OrderStatus(str, Enum):
    CREATED = "CREATED"
    ASSIGNED = "ASSIGNED"
    IN_PICKUP = "IN_PICKUP"
    IN_DELIVERY = "IN_DELIVERY"
    IN_DROP_OFF = "IN_DROP_OFF"
    COMPLETED = "COMPLETED"
    CANCELED = "CANCELED"


class OrderObservation(BaseModel):
    id: str
    client_id: str
    from_location: Location
    to_location: Location
    creation_time: int
    time_window: list[tuple[int, int]]
    status: OrderStatus


class ServiceStationObservation(BaseModel):
    id: str
    location: Location


class Bounds(BaseModel):
    min: Location
    max: Location


class Observation(BaseModel):
    current_time: int
    bounds: Bounds
    workers: list[WorkerObservation]
    orders: list[OrderObservation]
    service_stations: list[ServiceStationObservation]


class Metric(BaseModel):
    name: str
    value: float
    unit: str


class Info(BaseModel):
    simulation_id: str
    start_time: int
    end_time: int
    metrics: list[Metric]


class RenderRequest(BaseModel):
    observation: Observation
    info: Info


class RenderStatus(str, Enum):
    OK = "OK"
    ERROR = "ERROR"


class RenderResponse(BaseModel):
    status: RenderStatus


class RunStatus(str, Enum):
    CREATED = "CREATED"
    RUNNING = "RUNNING"
    COMPLETED = "COMPLETED"
    ERROR = "ERROR"


class SolveResponse(BaseModel):
    status: RunStatus
    message: str
    run_id: str


class RunThumbnail(BaseModel):
    id: str
    name: str
    creation_time: str
    status: RunStatus
    message: str


class RunDescription(BaseModel):
    name: str
    creation_time: str
    status: RunStatus
    message: str
    logistics_environment: str
    location_mode: str


class OrderInfo(BaseModel):
    id: str
    client_id: str
    from_location: Location
    to_location: Location
    creation_time: int
    time_window: list[tuple[int, int]]
    status: OrderStatus
    assignment_time: Optional[int]
    pickup_start_time: Optional[int]
    pickup_end_time: Optional[int]
    drop_off_start_time: Optional[int]
    drop_off_end_time: Optional[int]
    completion_time: Optional[int]
    assigned_worker_id: Optional[str]


class WorkerInfo(BaseModel):
    id: str
    travel_type: WorkerTravelType
    speed: float
    color: str
    status_history: list[tuple[int, WorkerStatus]]
    n_assigned_orders: int
    n_completed_orders: int
    completion_rate: float
    idle_rate: float
    with_order_rate: float
    traveled_distance: float
    consumed_fuel: float
    n_service_station_visits: int


class ServiceStationInfo(BaseModel):
    id: str
    location: Location
    service_events: list[tuple[str, int, int]]


class RunReport(BaseModel):
    id: str
    description: RunDescription
    start_time: Optional[int]
    end_time: Optional[int]
    orders: list[OrderInfo]
    workers: list[WorkerInfo]
    service_stations: list[ServiceStationInfo]
    metrics: list[Metric]


class InputValidationResponse(BaseModel):
    status: str
    observation: Optional[Observation]
