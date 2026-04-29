
from dataclasses import dataclass
from typing import Optional
from LogisticsDispatch.Domain.Entities.base_entity import BaseEntity
from LogisticsDispatch.Domain.Entities.enums import ShipmentStatus

@dataclass
class Shipment(BaseEntity):
    client_id: int = 0
    destination: str = ""
    weight_kg: float = 0.0
    status: ShipmentStatus = ShipmentStatus.PENDING
    assigned_vehicle_id: Optional[int] = None
    assigned_driver_id: Optional[int] = None

    def validate(self) -> None:
        if self.client_id <= 0:
            raise ValueError("client_id must be > 0.")
        if not self.destination.strip():
            raise ValueError("destination is required.")
        if self.weight_kg <= 0:
            raise ValueError("weight_kg must be > 0.")
