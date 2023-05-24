from abc import ABC, abstractmethod

from model.serviceable.serviceable import Serviceable
from model.car.engine.engine import Engine
from model.car.battery.battery import Battery
from model.car.tires.tires import Tires


class Car(Serviceable):
    def __init__(self, engine: Engine, battery: Battery, tires: Tires) -> None:
        self.__engine = engine
        self.__battery = battery
        self.__tires = tires

    def need_service(self) -> bool:
        return self.__engine.needs_service() or self.__battery.needs_service() or self.__tires.needs_service()
