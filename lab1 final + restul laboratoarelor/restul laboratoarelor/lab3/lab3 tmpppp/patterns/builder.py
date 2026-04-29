from abc import ABC, abstractmethod
from patterns.models import Shipment

class ShipmentBuilder(ABC):
    def __init__(self):
        self._shipment: Shipment | None = None

    @abstractmethod
    def create(self, shipment_id: int, destination: str, weight_kg: float) -> None: ...
    @abstractmethod
    def set_fragile(self, value: bool) -> None: ...
    @abstractmethod
    def set_insurance(self, value: float) -> None: ...
    @abstractmethod
    def set_temp_control(self, value: bool) -> None: ...
    @abstractmethod
    def set_priority(self, value: str) -> None: ...

    def build(self) -> Shipment:
        assert self._shipment is not None
        return self._shipment

class StandardShipmentBuilder(ShipmentBuilder):
    def create(self, shipment_id: int, destination: str, weight_kg: float) -> None:
        self._shipment = Shipment(id=shipment_id, destination=destination, weight_kg=weight_kg)

    def set_fragile(self, value: bool) -> None:
        self._shipment.fragile = value  # type: ignore

    def set_insurance(self, value: float) -> None:
        self._shipment.insurance_value = value  # type: ignore

    def set_temp_control(self, value: bool) -> None:
        self._shipment.temp_control = value  # type: ignore

    def set_priority(self, value: str) -> None:
        self._shipment.priority = value  # type: ignore

class ExpressShipmentBuilder(StandardShipmentBuilder):
    pass

class ShipmentDirector:
    def construct_standard(self, builder: ShipmentBuilder, shipment_id: int, destination: str, weight_kg: float) -> None:
        builder.create(shipment_id, destination, weight_kg)
        builder.set_priority("Normal")
        builder.set_fragile(False)
        builder.set_insurance(0.0)
        builder.set_temp_control(False)

    def construct_express(self, builder: ShipmentBuilder, shipment_id: int, destination: str, weight_kg: float) -> None:
        builder.create(shipment_id, destination, weight_kg)
        builder.set_priority("Express")
        builder.set_fragile(True)
        builder.set_insurance(2000.0)
        builder.set_temp_control(False)
