from dataclasses import dataclass

@dataclass
class Shipment:
    id: int
    destination: str
    weight_kg: float
    distance_km: float
    tracking_code: str

    def validate(self) -> None:
        if self.id <= 0:
            raise ValueError("id must be > 0")
        if not self.destination.strip():
            raise ValueError("destination required")
        if self.weight_kg <= 0:
            raise ValueError("weight_kg must be > 0")
        if self.distance_km <= 0:
            raise ValueError("distance_km must be > 0")
        if not self.tracking_code.strip():
            raise ValueError("tracking_code required")
