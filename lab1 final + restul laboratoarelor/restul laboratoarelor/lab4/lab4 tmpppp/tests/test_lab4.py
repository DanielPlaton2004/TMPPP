import unittest
from patterns.adapter import OldCarrierApi, OldCarrierAdapter
from patterns.composite import ShipmentLeaf, ShipmentGroup
from patterns.facade import DispatchFacade

class TestLab4(unittest.TestCase):
    def test_adapter(self):
        provider = OldCarrierAdapter(OldCarrierApi())
        result = provider.get_status("X")
        self.assertIn("X", result)

    def test_composite(self):
        group = ShipmentGroup("G")
        group.add(ShipmentLeaf("A", 10, 2))
        group.add(ShipmentLeaf("B", 5, 2))
        self.assertEqual(group.total_cost(), 30)

    def test_facade(self):
        facade = DispatchFacade()
        result = facade.book_and_dispatch("C", "D", 10, "T1")
        self.assertEqual(result.shipment_code, "T1")

if __name__ == "__main__":
    unittest.main()
