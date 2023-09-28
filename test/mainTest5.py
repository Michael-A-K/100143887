import math

import main


def test1():
    assert math.fabs(main.blastArea(7.5) - 176.7) < 0.1


def test2():
    assert math.fabs(main.blastArea(10) - 314.2) < 0.1


def test3():
    assert math.fabs(main.blastArea(72.534) - 16528.5) < 0.1


def test4():
    assert math.fabs(main.blastArea(55) - 9503.3) < 0.1


def test5():
    assert math.fabs(main.blastArea(101) - 32047.4) < 0.1


def test6():
    assert math.fabs(main.blastArea(99.952) - 31385.7) < 0.1


def test7():
    assert math.fabs(main.blastArea(100) - 31415.9) < 0.1
