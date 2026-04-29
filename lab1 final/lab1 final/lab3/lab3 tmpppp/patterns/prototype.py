import copy
from dataclasses import dataclass, field
from typing import Dict, List

@dataclass
class ShipmentTemplate:
    destination: str
    fragile: bool = False
    insurance_value: float = 0.0
    temp_control: bool = False
    metadata: Dict[str, List[str]] = field(default_factory=lambda: {"tags": ["TEMPLATE"]})

    def clone_shallow(self, new_id: int):
        cloned = copy.copy(self)
        return MaterializedShipment(
            id=new_id,
            destination=cloned.destination,
            fragile=cloned.fragile,
            insurance_value=cloned.insurance_value,
            temp_control=cloned.temp_control,
            metadata=cloned.metadata,
        )

    def clone_deep(self, new_id: int):
        cloned = copy.deepcopy(self)
        return MaterializedShipment(
            id=new_id,
            destination=cloned.destination,
            fragile=cloned.fragile,
            insurance_value=cloned.insurance_value,
            temp_control=cloned.temp_control,
            metadata=cloned.metadata,
        )

@dataclass
class MaterializedShipment:
    id: int
    destination: str
    fragile: bool
    insurance_value: float
    temp_control: bool
    metadata: Dict[str, List[str]]
