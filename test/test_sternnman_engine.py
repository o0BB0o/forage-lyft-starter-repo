import unittest
from sternman_engine import SternmanEngine

class TestSternmanEngine(unittest.TestCase):
    def test_needs_service_true(self):
        warning_light = True

        engine = SternmanEngine(warning_light)
        self.assertTrue(engine.needs_service())

    def test_needs_service_false(self):
        warning_light = False

        engine = SternmanEngine(warning_light)
        self.assertFalse(engine.needs_service())