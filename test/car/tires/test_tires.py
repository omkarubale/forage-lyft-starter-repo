import unittest
import array as arr

from model.car.tires.carrigan_tires import CarriganTires
from model.car.tires.octoprime_tires import OctoprimeTires


class TestCarriganTires(unittest.TestCase):
    def test_no_degradation(self):
        tires_array = arr.array([0, 0, 0, 0])
        tires = CarriganTires(tires)

        self.assertFalse(tires.needs_service())

    def test_one_tire_fail(self):
        tires_array = arr.array([0.9, 0, 0, 0])
        tires = CarriganTires(tires)

        self.assertTrue(tires.needs_service())

        tires_array = arr.array([0, 0.9, 0, 0])
        tires = CarriganTires(tires)

        self.assertTrue(tires.needs_service())

        tires_array = arr.array([0, 0, 0.9, 0])
        tires = CarriganTires(tires)

        self.assertTrue(tires.needs_service())

        tires_array = arr.array([0, 0, 0, 0.9])
        tires = CarriganTires(tires)

        self.assertTrue(tires.needs_service())

    def test_two_tires_fail(self):
        tires_array = arr.array([0.9, 0, 0.9, 0])
        tires = CarriganTires(tires)

        self.assertTrue(tires.needs_service())

    def test_three_tires_fail(self):
        tires_array = arr.array([0.9, 0.9, 0.9, 0])
        tires = CarriganTires(tires)

        self.assertTrue(tires.needs_service())

    def test_four_tires_fail(self):
        tires_array = arr.array([0.9, 0.9, 0.9, 0.9])
        tires = CarriganTires(tires)

        self.assertTrue(tires.needs_service())


class TestOctoprimeTires(unittest.TestCase):
    def test_no_degradation(self):
        tires_array = arr.array([0.9, 0, 0, 0])
        tires = OctoprimeTires(tires)

        self.assertFalse(tires.needs_service())

    def test_one_max_degradation(self):
        tires_array = arr.array([1, 0, 0, 0])
        tires = OctoprimeTires(tires)

        self.assertFalse(tires.needs_service())

    def test_two_max_degradation(self):
        tires_array = arr.array([1, 1, 0, 0])
        tires = OctoprimeTires(tires)

        self.assertFalse(tires.needs_service())

    def test_three_max_degradation(self):
        tires_array = arr.array([1, 1, 1, 0])
        tires = OctoprimeTires(tires)

        self.assertTrue(tires.needs_service())

    def test_high_degradation(self):
        tires_array = arr.array([0.75, 0.75, 0.75, 0.75])
        tires = OctoprimeTires(tires)

        self.assertTrue(tires.needs_service())
