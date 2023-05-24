from abc import ABC
import array as arr

from model.car.tires.tires import Tires


class OctoprimeTires(Tires):
    def __init__(self, tires) -> None:
        super().__init__()
        self.__tires = tires

    def needs_service(self) -> bool:
        total_degradation = 0.0

        for tire in self.__tires:
            total_degradation += tire

        if total_degradation >= 3:
            return True

        return False
