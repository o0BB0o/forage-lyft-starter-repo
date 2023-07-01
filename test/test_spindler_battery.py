import unittest
from datetime import date
from spindler_battery import SpindlerBattery


class TestSpindlerBattery(unittest.TestCase):
    def test_needs_service_true(self):
        curr_date = date("2023-01-01")
        last_date = date("2016-01-01")

        battery = SpindlerBattery(curr_date, last_date)
        self.assertTrue(battery.needs_service())

    def test_needs_service_false(self):
        curr_date = date("2023-01-01")
        last_date = date("2022-01-01")

        battery = SpindlerBattery(curr_date, last_date)
        self.assertFalse(battery.needs_service())