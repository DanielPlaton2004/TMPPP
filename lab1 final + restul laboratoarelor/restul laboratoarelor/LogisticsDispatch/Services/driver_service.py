
from LogisticsDispatch.Infrastructure.Repositories.repository_base import RepositoryBase
from LogisticsDispatch.Domain.Entities.driver import Driver
from LogisticsDispatch.Domain.Entities.vehicle_base import VehicleBase

class DriverService:
    """SRP: operații pentru șoferi."""

    def __init__(self, driver_repo: RepositoryBase[Driver], vehicle_repo: RepositoryBase[VehicleBase]):
        self._drivers = driver_repo
        self._vehicles = vehicle_repo

    def create(self, driver: Driver) -> None:
        driver.validate()
        if driver.vehicle_id is not None and self._vehicles.get_by_id(driver.vehicle_id) is None:
            raise ValueError("Vehicle not found for vehicle_id.")
        self._drivers.add(driver)

    def list_all(self):
        return self._drivers.get_all()

    def assign_vehicle(self, driver_id: int, vehicle_id: int) -> bool:
        d = self._drivers.get_by_id(driver_id)
        v = self._vehicles.get_by_id(vehicle_id)
        if not d or not v:
            return False
        d.vehicle_id = vehicle_id
        d.touch()
        self._drivers.update(d)
        return True
