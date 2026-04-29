
from LogisticsDispatch.Domain.Entities.enums import ShipmentStatus
from LogisticsDispatch.Infrastructure.Repositories.repository_base import RepositoryBase
from LogisticsDispatch.Domain.Entities.shipment import Shipment
from LogisticsDispatch.Domain.Entities.driver import Driver
from LogisticsDispatch.Services.fleet_service import FleetService
from LogisticsDispatch.Services.notifier import Notifier
from LogisticsDispatch.Services.billing_service import BillingService

class DispatchService:
    """SRP: coordonează procesul de dispatch."""

    def __init__(
        self,
        shipment_repo: RepositoryBase[Shipment],
        driver_repo: RepositoryBase[Driver],
        fleet_service: FleetService,
        notifier: Notifier,
        billing_service: BillingService,
        price_per_kg: float = 2.5,
    ):
        self._shipments = shipment_repo
        self._drivers = driver_repo
        self._fleet = fleet_service
        self._notifier = notifier
        self._billing = billing_service
        self._price_per_kg = price_per_kg

    def assign_and_dispatch(self, shipment_id: int) -> bool:
        shipment = self._shipments.get_by_id(shipment_id)
        if not shipment:
            print("❌ Shipment not found.")
            return False

        if shipment.status not in (ShipmentStatus.PENDING, ShipmentStatus.ASSIGNED):
            print(f"⚠️ Shipment status is '{shipment.status.value}', cannot dispatch.")
            return False

        vehicle = self._fleet.find_available_vehicle(shipment.weight_kg)
        if not vehicle:
            print("❌ No available vehicle with enough capacity.")
            return False

        driver = None
        for d in self._drivers.get_all():
            if d.vehicle_id == vehicle.id:
                driver = d
                break

        shipment.assigned_vehicle_id = vehicle.id
        shipment.assigned_driver_id = driver.id if driver else None
        shipment.status = ShipmentStatus.IN_TRANSIT
        shipment.touch()
        self._shipments.update(shipment)

        vehicle.available = False
        vehicle.touch()

        # polimorfism
        vehicle.deliver(shipment)

        who = driver.name if driver else "Unassigned driver"
        self._notifier.notify(f"Shipment #{shipment.id} dispatched with {vehicle.plate} ({who}).")

        invoice = self._billing.create_invoice(shipment_id=shipment.id, amount=shipment.weight_kg * self._price_per_kg)
        self._notifier.notify(f"Invoice #{invoice.id} created: {invoice.amount:.2f} ({invoice.status.value}).")

        shipment.status = ShipmentStatus.DELIVERED
        shipment.touch()
        self._shipments.update(shipment)

        vehicle.available = True
        vehicle.touch()
        return True

    def cancel(self, shipment_id: int) -> bool:
        shipment = self._shipments.get_by_id(shipment_id)
        if not shipment:
            return False
        if shipment.status == ShipmentStatus.DELIVERED:
            return False
        shipment.status = ShipmentStatus.CANCELLED
        shipment.touch()
        self._shipments.update(shipment)
        self._notifier.notify(f"Shipment #{shipment.id} cancelled.")
        return True
