
from abc import ABC, abstractmethod
from dataclasses import dataclass
from LogisticsDispatch.Domain.Entities.base_entity import BaseEntity
from LogisticsDispatch.Domain.Entities.enums import VehicleType

@dataclass
class VehicleBase(BaseEntity, ABC):
    plate: str = ""
    capacity_kg: float = 0.0
    available: bool = True
    vehicle_type: VehicleType = VehicleType.TRUCK

    def validate(self) -> None:
        if not self.plate.strip():
            raise ValueError("Plate is required.")
        if self.capacity_kg <= 0:
            raise ValueError("Capacity must be > 0.")

    def can_handle(self, weight: float) -> bool:
        return self.available and weight <= self.capacity_kg

    @abstractmethod
    def deliver(self, shipment) -> None:
        pass
