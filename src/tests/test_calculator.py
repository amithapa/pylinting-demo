import unittest
from app.calculator import Calculator


def test_add():
    sum = Calculator().add(2, 3)
    assert sum == 5


def test_subtract():
    diff = Calculator().difference(5, 2)
    assert diff == 3
