from abc import ABC, abstractmethod
from domain.shipment import Shipment

class PricingService(ABC):
    @abstractmethod
    def calculate_cost(self, shipment: Shipment) -> float: ...

class TrackingService(ABC):
    @abstractmethod
    def get_status(self, tracking_code: str) -> str: ...

class DocumentService(ABC):
    @abstractmethod
    def generate_awb(self, shipment: Shipment) -> str: ...

    @abstractmethod
    def generate_invoice(self, shipment: Shipment, amount: float) -> str: ...

    @abstractmethod
    def generate_label(self, shipment: Shipment) -> str: ...


# ===== Local carrier products =====
class LocalPricing(PricingService):
    # MD: tarif simplu (2.0 lei/kg + 0.5 lei/km)
    def calculate_cost(self, shipment: Shipment) -> float:
        shipment.validate()
        return shipment.weight_kg * 2.0 + shipment.distance_km * 0.5

class LocalTracking(TrackingService):
    def get_status(self, tracking_code: str) -> str:
        return f"[LOCAL] {tracking_code}: IN_TRANSIT"

class LocalDocs(DocumentService):
    def generate_awb(self, shipment: Shipment) -> str:
        return f"AWB(Local) #{shipment.id} | Dest={shipment.destination} | W={shipment.weight_kg}kg | TRK={shipment.tracking_code}"

    def generate_invoice(self, shipment: Shipment, amount: float) -> str:
        return f"INVOICE(Local) for Shipment #{shipment.id}: {amount:.2f} MDL"

    def generate_label(self, shipment: Shipment) -> str:
        return f"LABEL(Local) -> {shipment.destination} | Code={shipment.tracking_code}"


# ===== International carrier products =====
class IntlPricing(PricingService):
    # INTL: tarif mai mare + taxă fixă
    def calculate_cost(self, shipment: Shipment) -> float:
        shipment.validate()
        return 15.0 + shipment.weight_kg * 3.0 + shipment.distance_km * 0.8

class IntlTracking(TrackingService):
    def get_status(self, tracking_code: str) -> str:
        return f"[INTL] {tracking_code}: ARRIVED_AT_HUB"

class IntlDocs(DocumentService):
    def generate_awb(self, shipment: Shipment) -> str:
        return f"AWB(Intl) #{shipment.id} | Dest={shipment.destination} | W={shipment.weight_kg}kg | Customs=YES | TRK={shipment.tracking_code}"

    def generate_invoice(self, shipment: Shipment, amount: float) -> str:
        return f"INVOICE(Intl) for Shipment #{shipment.id}: {amount:.2f} EUR(eq)"

    def generate_label(self, shipment: Shipment) -> str:
        return f"LABEL(Intl) -> {shipment.destination} | Barcode={shipment.tracking_code}"
