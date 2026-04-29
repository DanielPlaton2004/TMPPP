
from dataclasses import dataclass
from LogisticsDispatch.Domain.Entities.base_entity import BaseEntity

@dataclass
class Client(BaseEntity):
    name: str = ""
    phone: str = ""

    def validate(self) -> None:
        if not self.name.strip():
            raise ValueError("Client name is required.")
        if not self.phone.strip():
            raise ValueError("Client phone is required.")
