from abc import ABC, abstractmethod

from model.serviceable.serviceable import Serviceable
from model.car.battery.battery import Battery
from model.car.engine.engine import Engine


class Car(Serviceable):
    def __init__(self, engine: Engine, battery: Battery) -> None:
        self.engine = engine
        self.battery = battery

    def need_service(self) -> bool:
        return self.engine.needs_service() or self.battery.needs_service()
