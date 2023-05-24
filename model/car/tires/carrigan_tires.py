from abc import ABC
import array as arr

from model.car.tires.tires import Tires


class CarriganTires(Tires):
    def __init__(self, tires) -> None:
        super().__init__()
        self.__tires = tires

    def needs_service(self) -> bool:
        for tire in self.__tires:
            if tire > 0.9:
                return True

        return False
