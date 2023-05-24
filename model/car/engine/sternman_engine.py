from abc import ABC

from model.car.engine.engine import Engine


class SternmanEngine(Engine):
    def __init__(self, warning_light_on: bool) -> None:
        super().__init__()
        self.__warning_light_on = warning_light_on

    def needs_service(self) -> bool:
        # doing the if-true return true else return false because python is not strongly typed
        if self.__warning_light_on:
            return True
        else:
            return False
