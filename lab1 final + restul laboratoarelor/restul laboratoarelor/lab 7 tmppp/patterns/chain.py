from dataclasses import dataclass
from typing import Optional

@dataclass
class ShipmentRequest:
    weight_kg: float
    insurance_value: float
    destination: str

class Handler:
    def __init__(self):
        self._next: Optional["Handler"] = None
    def set_next(self, nxt: "Handler") -> "Handler":
        self._next = nxt; return nxt
    def handle(self, req: ShipmentRequest) -> str:
        return self._next.handle(req) if self._next else "✅ Approved"

class WeightHandler(Handler):
    def handle(self, req: ShipmentRequest) -> str:
        if req.weight_kg > 12000: return "❌ Rejected: weight too high"
        return super().handle(req)

class InsuranceHandler(Handler):
    def handle(self, req: ShipmentRequest) -> str:
        if req.insurance_value < 0: return "❌ Rejected: invalid insurance"
        return super().handle(req)

class ComplianceHandler(Handler):
    def handle(self, req: ShipmentRequest) -> str:
        if not req.destination.strip(): return "❌ Rejected: missing destination"
        return super().handle(req)
