import unittest
from patterns.flyweight import AddressFlyweightFactory
from patterns.proxy import DispatchService, DispatchServiceProxy

class T(unittest.TestCase):
    def test_flyweight(self):
        f = AddressFlyweightFactory()
        self.assertIs(f.get("A","B","C"), f.get("A","B","C"))
        self.assertEqual(f.pool_size(), 1)
    def test_proxy(self):
        self.assertIn("denied", DispatchServiceProxy(DispatchService(), "guest").dispatch("X"))

if __name__ == "__main__":
    unittest.main()
