from abc import ABC, abstractmethod
from patterns.vehicle_products import Vehicle, Truck, Van, ReeferTruck

class VehicleFactory(ABC):
    """Creator (Factory Method): definește metoda de fabrică."""

    @abstractmethod
    def create_vehicle(self, vehicle_id: int, plate: str, capacity_kg: float) -> Vehicle:
        pass

class TruckFactory(VehicleFactory):
    def create_vehicle(self, vehicle_id: int, plate: str, capacity_kg: float) -> Vehicle:
        v = Truck(id=vehicle_id, plate=plate, capacity_kg=capacity_kg)
        v.validate()
        return v

class VanFactory(VehicleFactory):
    def create_vehicle(self, vehicle_id: int, plate: str, capacity_kg: float) -> Vehicle:
        v = Van(id=vehicle_id, plate=plate, capacity_kg=capacity_kg)
        v.validate()
        return v

class ReeferTruckFactory(VehicleFactory):
    def create_vehicle(self, vehicle_id: int, plate: str, capacity_kg: float) -> Vehicle:
        v = ReeferTruck(id=vehicle_id, plate=plate, capacity_kg=capacity_kg, temperature_c=2.0)
        v.validate()
        return v
