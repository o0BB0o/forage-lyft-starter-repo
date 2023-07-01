from car import Car
from nubbin_battery import NubbinBattery
from spindler_battery import SpindlerBattery
from capulet_engine import CapuletEngine
from sternman_engine import SternmanEngine
from willoughby_engine import WilloughbyEngine


class CarFactory:
    def create_calliope(curr_date, last_date, curr_mileage, last_mileage):
        engine = CapuletEngine(curr_mileage, last_mileage)
        battery = SpindlerBattery(curr_date, last_date)
        car = Car(engine, battery)
        return car

    def create_glissade(curr_date, last_date, curr_mileage, last_mileage):
        engine = WilloughbyEngine(curr_mileage, last_mileage)
        battery = SpindlerBattery(curr_date, last_date)
        car = Car(engine, battery)
        return car

    def create_palindrome(curr_date, last_date, warning_light_is_on):
        engine = SternmanEngine(warning_light_is_on)
        battery = SpindlerBattery(curr_date, last_date)
        car = Car(engine, battery)
        return car

    def create_rorschach(curr_date, last_date, curr_mileage, last_mileage):
        engine = WilloughbyEngine(curr_mileage, last_mileage)
        battery = NubbinBattery(curr_date, last_date)
        car = Car(engine, battery)
        return car

    def create_thovex(curr_date, last_date, curr_mileage, last_mileage):
        engine = CapuletEngine(curr_mileage, last_mileage)
        battery = NubbinBattery(curr_date, last_date)
        car = Car(engine, battery)
        return car