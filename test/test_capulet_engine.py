import unittest
from capulet_engine import CapuletEngine


class TestCapuletEngine(unittest.TestCase):
    def test_needs_service_true(self):
        curr_milage = 50000
        last_mileage = 10000

        engine = CapuletEngine(curr_milage, last_mileage)
        self.assertTrue(engine.needs_service())

    def test_needs_service_false(self):
        curr_milage = 20000
        last_mileage = 0

        engine = CapuletEngine(curr_milage, last_mileage)
        self.assertFalse(engine.needs_service())