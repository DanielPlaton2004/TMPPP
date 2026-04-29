import unittest
from patterns.strategy import RoutePlanner, FastestRouteStrategy, CheapestRouteStrategy
from patterns.iterator import ShipmentCollection
from patterns.command import DispatchCommand, CommandInvoker

class T(unittest.TestCase):
    def test_strategy(self):
        p = RoutePlanner(FastestRouteStrategy())
        self.assertIn("Fastest", p.plan("A","B"))
        p.set_strategy(CheapestRouteStrategy())
        self.assertIn("Cheapest", p.plan("A","B"))
    def test_undo(self):
        c = ShipmentCollection(["S1"])
        inv = CommandInvoker()
        inv.execute(DispatchCommand(c,"S2"))
        self.assertIn("S2", c.snapshot())
        inv.undo()
        self.assertNotIn("S2", c.snapshot())

if __name__ == "__main__":
    unittest.main()
