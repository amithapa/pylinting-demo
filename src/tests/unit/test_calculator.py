import unittest
from app.calculator import add, difference


def test_add():
    sum = add(2, 3)
    assert sum == 5


def test_subtract():
    diff = difference(5, 2)
    assert diff == 3
