from abc import ABC, abstractmethod
from patterns.carrier_products import (
    PricingService, TrackingService, DocumentService,
    LocalPricing, LocalTracking, LocalDocs,
    IntlPricing, IntlTracking, IntlDocs
)

class CarrierToolkitFactory(ABC):
    """Abstract Factory: creează o familie de obiecte înrudite."""

    @abstractmethod
    def create_pricing_service(self) -> PricingService: ...
    @abstractmethod
    def create_tracking_service(self) -> TrackingService: ...
    @abstractmethod
    def create_document_service(self) -> DocumentService: ...

class LocalCarrierFactory(CarrierToolkitFactory):
    def create_pricing_service(self) -> PricingService:
        return LocalPricing()

    def create_tracking_service(self) -> TrackingService:
        return LocalTracking()

    def create_document_service(self) -> DocumentService:
        return LocalDocs()

class InternationalCarrierFactory(CarrierToolkitFactory):
    def create_pricing_service(self) -> PricingService:
        return IntlPricing()

    def create_tracking_service(self) -> TrackingService:
        return IntlTracking()

    def create_document_service(self) -> DocumentService:
        return IntlDocs()
