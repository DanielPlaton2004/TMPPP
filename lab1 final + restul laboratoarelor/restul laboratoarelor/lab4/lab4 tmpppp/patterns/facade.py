from dataclasses import dataclass
from patterns.adapter import TrackingProvider, OldCarrierApi, OldCarrierAdapter
from patterns.composite import ShipmentLeaf


@dataclass
class DispatchResult:
    shipment_code: str
    status: str
    estimated_cost: float


class PricingService:
    def price_per_kg(self) -> float:
        return 2.5


class DispatchService:
    def dispatch(self, shipment_code: str) -> str:
        return f"Shipment {shipment_code} dispatched"


class DispatchFacade:
    def __init__(self):
        self._pricing = PricingService()
        self._dispatch = DispatchService()
        self._tracking: TrackingProvider = OldCarrierAdapter(OldCarrierApi())

    def book_and_dispatch(self, client: str, destination: str, weight_kg: float, tracking_code: str) -> DispatchResult:
        leaf = ShipmentLeaf(code=tracking_code, weight_kg=weight_kg, price_per_kg=self._pricing.price_per_kg())
        cost = leaf.total_cost()
        status = self._dispatch.dispatch(tracking_code)
        tracking = self._tracking.get_status(tracking_code)
        return DispatchResult(
            shipment_code=tracking_code,
            status=f"{status} | {tracking}",
            estimated_cost=cost,
        )
