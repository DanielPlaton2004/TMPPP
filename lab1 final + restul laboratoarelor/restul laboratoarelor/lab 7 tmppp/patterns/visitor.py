from dataclasses import dataclass
from abc import ABC, abstractmethod
from typing import List

@dataclass
class Shipment:
    code: str
    destination: str
    weight_kg: float

class ExportVisitor(ABC):
    @abstractmethod
    def export(self, shipments: List[Shipment]) -> str: ...

class CsvExportVisitor(ExportVisitor):
    def export(self, shipments: List[Shipment]) -> str:
        lines=["code,destination,weight_kg"]
        for s in shipments:
            lines.append(f"{s.code},{s.destination},{s.weight_kg}")
        return "\n".join(lines)

class XmlExportVisitor(ExportVisitor):
    def export(self, shipments: List[Shipment]) -> str:
        parts=["<shipments>"]
        for s in shipments:
            parts.append(f'  <shipment code="{s.code}"><dest>{s.destination}</dest><w>{s.weight_kg}</w></shipment>')
        parts.append("</shipments>")
        return "\n".join(parts)
