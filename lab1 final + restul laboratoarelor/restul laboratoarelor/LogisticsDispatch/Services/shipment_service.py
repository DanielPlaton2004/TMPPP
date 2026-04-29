
from LogisticsDispatch.Infrastructure.Repositories.repository_base import RepositoryBase
from LogisticsDispatch.Domain.Entities.shipment import Shipment
from LogisticsDispatch.Domain.Entities.client import Client

class ShipmentService:
    """SRP: operații pentru shipments (comenzi transport)."""

    def __init__(self, shipment_repo: RepositoryBase[Shipment], client_repo: RepositoryBase[Client]):
        self._shipments = shipment_repo
        self._clients = client_repo

    def create(self, shipment: Shipment) -> None:
        shipment.validate()
        if self._clients.get_by_id(shipment.client_id) is None:
            raise ValueError("Client not found for client_id.")
        self._shipments.add(shipment)

    def list_all(self):
        return self._shipments.get_all()

    def get(self, shipment_id: int):
        return self._shipments.get_by_id(shipment_id)

    def delete(self, shipment_id: int) -> bool:
        return self._shipments.remove(shipment_id)
