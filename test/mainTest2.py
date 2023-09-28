import math
import main


def test1():
    assert math.fabs(main.trapArea(3, 3, 3) - 9.0) < 0.1


def test2():
    assert math.fabs(main.trapArea(5, 6, 7) - 38.5) < 0.1


def test3():
    assert math.fabs(main.trapArea(7, 10, 6) - 51.0) < 0.1


def test4():
    assert math.fabs(main.trapArea(13, 9, 3) - 33.0) < 0.1


def test5():
    assert math.fabs(main.trapArea(6, 11, 4) - 34.0) < 0.1


def test6():
    assert math.fabs(main.trapArea(11, 8, 5) - 47.5) < 0.1
