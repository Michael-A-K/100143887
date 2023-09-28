import math

import main


def test1():
    assert math.fabs(main.conicVol(4, 4) - 67.02) < 0.01


def test2():
    assert math.fabs(main.conicVol(4, 3) - 50.27) < 0.01


def test3():
    assert math.fabs(main.conicVol(9, 3) - 254.47) < 0.01


def test4():
    assert math.fabs(main.conicVol(1, 3) - 3.14) < 0.01


def test5():
    assert math.fabs(main.conicVol(1, 5) - 5.24) < 0.01


def test6():
    assert math.fabs(main.conicVol(7, 7) - 359.19) < 0.01


def test7():
    assert math.fabs(main.conicVol(1.5, 3) - 7.07) < 0.01


def test8():
    assert math.fabs(main.conicVol(1.5, 5) - 11.78) < 0.01
