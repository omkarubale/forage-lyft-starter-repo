from abc import ABC

from model.car.engine.engine import Engine


class CapuletEngine(Engine):
    def __init__(self, last_service_mileage, current_mileage) -> None:
        super().__init__()
        self.__current_mileage = current_mileage
        self.__last_service_mileage = last_service_mileage

    def needs_service(self) -> bool:
        return self.__current_mileage - self.__last_service_mileage > 30000
