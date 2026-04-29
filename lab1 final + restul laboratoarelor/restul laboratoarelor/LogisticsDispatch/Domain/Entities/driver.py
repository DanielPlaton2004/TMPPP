
from dataclasses import dataclass
from typing import Optional
from LogisticsDispatch.Domain.Entities.base_entity import BaseEntity

@dataclass
class Driver(BaseEntity):
    name: str = ""
    license_no: str = ""
    vehicle_id: Optional[int] = None

    def validate(self) -> None:
        if not self.name.strip():
            raise ValueError("Driver name is required.")
        if not self.license_no.strip():
            raise ValueError("Driver license_no is required.")
