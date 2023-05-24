import unittest
from abc import abstractmethod, ABC

from model.car.engine.capulet_engine import CapuletEngine
from model.car.engine.sternman_engine import SternmanEngine
from model.car.engine.willoughby_engine import WilloughbyEngine


class TestAbstractMileageEngine(ABC, unittest.TestCase):
    @abstractmethod
    def get_threshold_mileage(self):
        pass

    def test_doesnt_need_service_small_difference(self):
        engine = CapuletEngine(20000, 20001)
        self.assertFalse(engine.needs_service())

    def test_doesnt_need_service_big_difference(self):
        engine = CapuletEngine(20000, 20000 + self.get_threshold_mileage() - 1)
        self.assertFalse(engine.needs_service())

    def test_current_mileage_equal_service_mileage(self):
        engine = CapuletEngine(20000, 20000)
        self.assertFalse(engine.needs_service())

    def test_service_mileage_greater_than_current_mileage(self):
        engine = CapuletEngine(20000, 19999)
        self.assertFalse(engine.needs_service())

    def test_doesnt_need_service_exact_match(self):
        engine = CapuletEngine(20000, 20000 + self.get_threshold_mileage())
        self.assertFalse(engine.needs_service())

    def test_needs_service_small_difference(self):
        engine = CapuletEngine(20000, 20000 + self.get_threshold_mileage() + 1)
        self.assertTrue(engine.needs_service())

    def test_needs_service_big_difference(self):
        engine = CapuletEngine(
            20000, 20000 + self.get_threshold_mileage() + 50000)
        self.assertTrue(engine.needs_service())

    def test_negative_current_mileage(self):
        engine = CapuletEngine(-20000, -20000 +
                               self.get_threshold_mileage() + 1)
        self.assertFalse(engine.needs_service())

    def test_negative_service_mileage(self):
        engine = CapuletEngine(-20000, 10000 + self.get_threshold_mileage())
        self.assertFalse(engine.needs_service())


class TestCapuletEngine(TestAbstractMileageEngine):
    # have to test: current mileage - service mileage > 30000 -> true
    def get_threshold_mileage(self):
        return 30000


class TestWilloughbyEngine(TestAbstractMileageEngine):
    # have to test: current mileage - service mileage > 60000 -> true
    def get_threshold_mileage(self):
        return 60000


class TestSternmanEngine(unittest.TestCase):
    # have to test: warning light on -> true

    def test_needs_service(self):
        engine = SternmanEngine(True)
        self.assertTrue(engine.needs_service())

    def test_doesnt_needs_service(self):
        engine = SternmanEngine(False)
        self.assertFalse(engine.needs_service())
