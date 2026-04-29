from dataclasses import dataclass, field
from typing import Dict, List

@dataclass
class Shipment:
    id: int
    destination: str
    weight_kg: float
    fragile: bool = False
    insurance_value: float = 0.0
    temp_control: bool = False
    priority: str = "Normal"
    metadata: Dict[str, List[str]] = field(default_factory=lambda: {"tags": []})
