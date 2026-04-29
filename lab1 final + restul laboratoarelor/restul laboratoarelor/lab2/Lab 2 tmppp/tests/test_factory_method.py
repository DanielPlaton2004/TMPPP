import unittest
from patterns.factory_method import TruckFactory, VanFactory, ReeferTruckFactory
from patterns.vehicle_products import Truck, Van, ReeferTruck

class TestFactoryMethod(unittest.TestCase):
    def test_truck_factory(self):
        v = TruckFactory().create_vehicle(1, "TR-1", 1000)
        self.assertIsInstance(v, Truck)

    def test_van_factory(self):
        v = VanFactory().create_vehicle(2, "VN-2", 500)
        self.assertIsInstance(v, Van)

    def test_reefer_factory(self):
        v = ReeferTruckFactory().create_vehicle(3, "RF-3", 2000)
        self.assertIsInstance(v, ReeferTruck)

if __name__ == "__main__":
    unittest.main()
