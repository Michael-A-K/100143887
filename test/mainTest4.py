import math

import main


def test1():
    assert math.fabs(main.cubicBarrier(112) - 75264.0) < 0.1


def test2():
    assert math.fabs(main.cubicBarrier(4) - 96.0) < 0.1


def test3():
    assert math.fabs(main.cubicBarrier(33) - 6534.0) < 0.1


def test4():
    assert math.fabs(main.cubicBarrier(50) - 15000.0) < 0.1


def test5():
    assert math.fabs(main.cubicBarrier(5) - 150.0) < 0.1


def test6():
    assert math.fabs(main.cubicBarrier(19) - 2166.0) < 0.1


def test7():
    assert math.fabs(main.cubicBarrier(111) - 73926.0) < 0.1
