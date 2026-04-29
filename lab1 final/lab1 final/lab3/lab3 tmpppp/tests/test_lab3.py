import unittest
from patterns.builder import ShipmentDirector, StandardShipmentBuilder
from patterns.prototype import ShipmentTemplate
from patterns.singleton import AppConfig

class TestLab3(unittest.TestCase):
    def test_builder(self):
        director = ShipmentDirector()
        builder = StandardShipmentBuilder()
        director.construct_standard(builder, 1, "Chișinău", 100)
        shipment = builder.build()
        self.assertEqual(shipment.priority, "Normal")

    def test_prototype(self):
        proto = ShipmentTemplate(destination="Bălți")
        shallow = proto.clone_shallow(1)
        deep = proto.clone_deep(2)
        shallow.metadata["tags"].append("X")
        self.assertIn("X", proto.metadata["tags"])
        deep.metadata["tags"].append("Y")
        self.assertNotIn("Y", proto.metadata["tags"])

    def test_singleton(self):
        self.assertIs(AppConfig.instance(), AppConfig.instance())

if __name__ == "__main__":
    unittest.main()
