import unittest
from datetime import datetime
from abc import abstractmethod, ABC

from model.car.battery.spindler_battery import SpindlerBattery


class TestAbstractBattery(ABC, unittest.TestCase):
    @abstractmethod
    def get_threshold_year(self):
        pass

    def test_doesnt_need_service_small_difference(self):
        today = datetime.today().date()
        last_service_date = today.replace(
            year=today.year - self.get_threshold_year())
        last_service_date = last_service_date.replace(day=today.day + 1)

        battery = SpindlerBattery(today, last_service_date)
        self.assertFalse(battery.needs_service())

    def test_needs_service_small_difference(self):
        today = datetime.today().date()
        last_service_date = today.replace(
            year=today.year - self.get_threshold_year())
        last_service_date = last_service_date.replace(day=today.day - 1)

        battery = SpindlerBattery(today, last_service_date)
        self.assertTrue(battery.needs_service())

    def test_doesnt_need_service_exact_match(self):
        today = datetime.today().date()
        last_service_date = today.replace(
            year=today.year - self.get_threshold_year())

        battery = SpindlerBattery(today, last_service_date)
        self.assertFalse(battery.needs_service())

    def test_current_date_before_service_date(self):
        today = datetime.today().date()
        last_service_date = today.replace(day=today.day + 1)

        battery = SpindlerBattery(today, last_service_date)
        self.assertFalse(battery.needs_service())

    def test_current_date_equal_service_date(self):
        today = datetime.today().date()
        last_service_date = today

        battery = SpindlerBattery(today, last_service_date)
        self.assertFalse(battery.needs_service())

    def test_needs_service_small_year_delta(self):
        today = datetime.today().date()
        last_service_date = today.replace(
            year=today.year - self.get_threshold_year() - 1)

        battery = SpindlerBattery(today, last_service_date)
        self.assertTrue(battery.needs_service())

    def test_doesnt_need_service_small_year_delta(self):
        today = datetime.today().date()
        last_service_date = today.replace(
            year=today.year - self.get_threshold_year() + 1)

        battery = SpindlerBattery(today, last_service_date)
        self.assertFalse(battery.needs_service())

    def test_needs_service_small_month_delta(self):
        today = datetime.today().date()
        last_service_date = today.replace(
            year=today.year - self.get_threshold_year())
        last_service_date = last_service_date.replace(month=today.month - 1)

        battery = SpindlerBattery(today, last_service_date)
        self.assertTrue(battery.needs_service())

    def test_doesnt_need_service_small_month_delta(self):
        today = datetime.today().date()
        last_service_date = today.replace(
            year=today.year - self.get_threshold_year())
        last_service_date = last_service_date.replace(month=today.month + 1)

        battery = SpindlerBattery(today, last_service_date)
        self.assertFalse(battery.needs_service())

    def test_needs_service_small_day_delta(self):
        today = datetime.today().date()
        last_service_date = today.replace(
            year=today.year - self.get_threshold_year())
        last_service_date = last_service_date.replace(day=today.day - 1)

        battery = SpindlerBattery(today, last_service_date)
        self.assertTrue(battery.needs_service())

    def test_doesnt_need_service_small_day_delta(self):
        today = datetime.today().date()
        last_service_date = today.replace(
            year=today.year - self.get_threshold_year())
        last_service_date = last_service_date.replace(day=today.day + 1)

        battery = SpindlerBattery(today, last_service_date)
        self.assertFalse(battery.needs_service())


class TestSpindlerBattery(TestAbstractBattery):
    # have to test: current_date - last_service_date > 2 years -> true
    def get_threshold_year(self):
        return 3


class TestNubbinBattery(TestAbstractBattery):
    # have to test: current_date - last_service_date > 4 years -> true
    def get_threshold_year(self):
        return 4
