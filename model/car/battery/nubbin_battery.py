from abc import ABC

from datetime import datetime

from model.car.battery.battery import Battery


class NubbinBattery(Battery):
    def __init__(self, last_service_date, current_date) -> None:
        super().__init__()
        self.__last_service_date = last_service_date
        self.__current_date = current_date

    def needs_service(self) -> bool:
        service_threshold_date = self.__last_service_date.replace(
            year=self.__last_service_date.year + 4)

        if service_threshold_date < datetime.today().date():
            return True
        else:
            return False
