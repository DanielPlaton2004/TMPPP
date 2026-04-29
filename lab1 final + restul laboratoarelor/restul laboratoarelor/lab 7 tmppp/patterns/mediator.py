from abc import ABC, abstractmethod
from typing import Optional

class Mediator(ABC):
    @abstractmethod
    def dispatch(self, code: str) -> None: ...

class DispatchMediator(Mediator):
    def __init__(self):
        self.driver: Optional["DriverColleague"]=None
        self.vehicle: Optional["VehicleColleague"]=None
        self.warehouse: Optional["WarehouseColleague"]=None
    def register(self, driver, vehicle, warehouse) -> None:
        self.driver=driver; self.vehicle=vehicle; self.warehouse=warehouse
    def dispatch(self, code: str) -> None:
        print(f"[MED] Start {code}")
        if self.warehouse: self.warehouse.prepare(code)
        if self.driver: self.driver.accept(code)
        if self.vehicle: self.vehicle.load(code)
        print(f"[MED] Done {code}")

class Colleague(ABC):
    def __init__(self, mediator: DispatchMediator): self._m=mediator

class DriverColleague(Colleague):
    def __init__(self, mediator, name: str): super().__init__(mediator); self.name=name
    def accept(self, code: str) -> None: print(f"Driver {self.name} accepts {code}")

class VehicleColleague(Colleague):
    def __init__(self, mediator, plate: str): super().__init__(mediator); self.plate=plate
    def load(self, code: str) -> None: print(f"Vehicle {self.plate} loads {code}")

class WarehouseColleague(Colleague):
    def __init__(self, mediator, wh: str): super().__init__(mediator); self.wh=wh
    def prepare(self, code: str) -> None: print(f"Warehouse {self.wh} prepares {code}")
