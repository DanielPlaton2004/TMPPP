
from dataclasses import dataclass
from LogisticsDispatch.Domain.Entities.vehicle_base import VehicleBase
from LogisticsDispatch.Domain.Entities.enums import VehicleType

@dataclass
class Truck(VehicleBase):
    vehicle_type: VehicleType = VehicleType.TRUCK

    def deliver(self, shipment) -> None:
        print(f"Truck {self.plate} delivers shipment #{shipment.id} -> {shipment.destination} (weight={shipment.weight_kg}kg)")
