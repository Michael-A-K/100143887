import math

import main


def test1():
    assert math.fabs(main.atmoShift(98.6) - 37.00) < 0.01


def test2():
    assert math.fabs(main.atmoShift(52.3) - 11.28) < 0.01


def test3():
    assert math.fabs(main.atmoShift(82.45) - 28.03) < 0.01


def test4():
    assert math.fabs(main.atmoShift(75) - 23.89) < 0.01


def test5():
    assert math.fabs(main.atmoShift(100) - 37.78) < 0.01
