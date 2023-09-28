import main


def test1():
    assert main.periRect(12, 5) == 34


def test2():
    assert main.periRect(131, 75) == 412


def test3():
    assert main.periRect(20, 25) == 90


def test4():
    assert main.periRect(9, 256) == 530


def test5():
    assert main.periRect(36, 72) == 216


def test6():
    assert main.periRect(8, 6) == 28


def test7():
    assert main.periRect(18, 16) == 68
