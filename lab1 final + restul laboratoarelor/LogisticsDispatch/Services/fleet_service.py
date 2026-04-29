
from typing import Optional
from LogisticsDispatch.Infrastructure.Repositories.repository_base import RepositoryBase
from LogisticsDispatch.Domain.Entities.vehicle_base import VehicleBase

class FleetService:
    """SRP: reguli flotă (găsește vehicul disponibil)."""

    def __init__(self, vehicle_repo: RepositoryBase[VehicleBase]):
        self._vehicles = vehicle_repo

    def add_vehicle(self, vehicle: VehicleBase) -> None:
        vehicle.validate()
        self._vehicles.add(vehicle)

    def list_all(self):
        return self._vehicles.get_all()

    def find_available_vehicle(self, weight_kg: float) -> Optional[VehicleBase]:
        for v in self._vehicles.get_all():
            if v.can_handle(weight_kg):
                return v
        return None
