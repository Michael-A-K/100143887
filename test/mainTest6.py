import math

import main


def test1():
    assert math.fabs(main.elevationVect(1, 9, 14, 2) - -0.54) < 0.01


def test2():
    assert math.fabs(main.elevationVect(1, 7, 18, 3) - -0.24) < 0.01


def test3():
    assert math.fabs(main.elevationVect(6, 4, 2, 2) - 0.50) < 0.01


def test4():
    assert math.fabs(main.elevationVect(4, 4, 5, 3) - -1.00) < 0.01


def test5():
    assert math.fabs(main.elevationVect(1, 1, 2, 9) - 8.00) < 0.01


def test6():
    assert math.fabs(main.elevationVect(1, 7, 2, 9) - 2.00) < 0.01
