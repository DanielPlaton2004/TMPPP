import unittest
from patterns.abstract_factory import LocalCarrierFactory, InternationalCarrierFactory
from domain.shipment import Shipment

class TestAbstractFactory(unittest.TestCase):
    def test_local_toolkit(self):
        f = LocalCarrierFactory()
        pricing = f.create_pricing_service()
        tracking = f.create_tracking_service()
        docs = f.create_document_service()

        s = Shipment(id=1, destination="Chișinău", weight_kg=10, distance_km=5, tracking_code="TRK-1")
        cost = pricing.calculate_cost(s)
        self.assertGreater(cost, 0)
        self.assertIn("LOCAL", tracking.get_status("TRK-1"))
        self.assertIn("AWB(Local)", docs.generate_awb(s))

    def test_intl_toolkit(self):
        f = InternationalCarrierFactory()
        pricing = f.create_pricing_service()
        s = Shipment(id=2, destination="Iași", weight_kg=10, distance_km=100, tracking_code="TRK-2")
        cost = pricing.calculate_cost(s)
        self.assertGreaterEqual(cost, 15.0)  # include taxă fixă

if __name__ == "__main__":
    unittest.main()
