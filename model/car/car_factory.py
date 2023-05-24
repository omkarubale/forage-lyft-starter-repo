from model.car.car import Car

from model.car.battery.nubbin_battery import NubbinBattery
from model.car.battery.spindler_battery import SpindlerBattery

from model.car.engine.capulet_engine import CapuletEngine
from model.car.engine.sternman_engine import SternmanEngine
from model.car.engine.willoughby_engine import WilloughbyEngine


class CarFactory():
    def __init__(self) -> None:
        pass

    def create_calliope(self, current_date, last_service_date, current_mileage: int, last_service_mileage: int) -> Car:
        return Car(CapuletEngine(last_service_mileage, current_mileage), SpindlerBattery(last_service_date, current_date))

    def create_glissade(self, current_date, last_service_date, current_mileage: int, last_service_mileage: int) -> Car:
        return Car(WilloughbyEngine(last_service_mileage, current_mileage), SpindlerBattery(last_service_date, current_date))

    def create_palindrome(self, current_date, last_service_date, warning_light_on: bool) -> Car:
        return Car(SternmanEngine(warning_light_on), SpindlerBattery(last_service_date, current_date))

    def create_rorschach(self, current_date, last_service_date, current_mileage, last_service_mileage) -> Car:
        return Car(WilloughbyEngine(last_service_mileage, current_mileage), NubbinBattery(last_service_date, current_date))

    def create_thovex(self, current_date, last_service_date, current_mileage, last_service_mileage) -> Car:
        return Car(CapuletEngine(last_service_mileage, current_mileage), NubbinBattery(last_service_date, current_date))
