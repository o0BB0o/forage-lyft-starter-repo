import unittest
from willoughby_engine import WilloughbyEngine


class TestWilloughbyEngine(unittest.TestCase):
    def test_needs_service_true(self):
        curr_milage = 80000
        last_mileage = 10000

        engine = WilloughbyEngine(curr_milage, last_mileage)
        self.assertTrue(engine.needs_service())

    def test_needs_service_false(self):
        curr_milage = 30000
        last_mileage = 0

        engine = WilloughbyEngine(curr_milage, last_mileage)
        self.assertFalse(engine.needs_service())