
from dataclasses import dataclass
from LogisticsDispatch.Domain.Entities.vehicle_base import VehicleBase
from LogisticsDispatch.Domain.Entities.enums import VehicleType

@dataclass
class Van(VehicleBase):
    vehicle_type: VehicleType = VehicleType.VAN

    def deliver(self, shipment) -> None:
        print(f"Van {self.plate} delivers shipment #{shipment.id} -> {shipment.destination} (weight={shipment.weight_kg}kg)")
