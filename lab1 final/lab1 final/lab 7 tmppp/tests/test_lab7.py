import unittest
from patterns.chain import WeightHandler, InsuranceHandler, ComplianceHandler, ShipmentRequest
from patterns.state import ShipmentContext
from patterns.visitor import Shipment, CsvExportVisitor

class T(unittest.TestCase):
    def test_chain(self):
        c = WeightHandler()
        c.set_next(InsuranceHandler()).set_next(ComplianceHandler())
        self.assertIn("Approved", c.handle(ShipmentRequest(1000,0,"X")))
    def test_state(self):
        s = ShipmentContext("S"); s.dispatch()
        self.assertEqual(s.status(), "IN_TRANSIT")
    def test_visitor(self):
        out = CsvExportVisitor().export([Shipment("S1","D",1)])
        self.assertIn("S1", out)

if __name__ == "__main__":
    unittest.main()
