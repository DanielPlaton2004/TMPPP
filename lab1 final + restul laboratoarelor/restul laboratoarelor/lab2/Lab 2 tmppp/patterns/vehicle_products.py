from abc import ABC, abstractmethod
from dataclasses import dataclass

@dataclass
class Vehicle(ABC):
    id: int
    plate: str
    capacity_kg: float

    def validate(self) -> None:
        if not self.plate.strip():
            raise ValueError("plate required")
        if self.capacity_kg <= 0:
            raise ValueError("capacity_kg must be > 0")

    def can_handle(self, weight_kg: float) -> bool:
        return weight_kg <= self.capacity_kg

    @abstractmethod
    def deliver(self, shipment_id: int, destination: str) -> str: ...

@dataclass
class Truck(Vehicle):
    def deliver(self, shipment_id: int, destination: str) -> str:
        return f"Truck {self.plate} delivers shipment #{shipment_id} -> {destination}"

@dataclass
class Van(Vehicle):
    def deliver(self, shipment_id: int, destination: str) -> str:
        return f"Van {self.plate} delivers shipment #{shipment_id} -> {destination}"

@dataclass
class ReeferTruck(Vehicle):
    temperature_c: float = 4.0

    def deliver(self, shipment_id: int, destination: str) -> str:
        return f"ReeferTruck {self.plate} delivers shipment #{shipment_id} -> {destination} (temp={self.temperature_c}C)"
