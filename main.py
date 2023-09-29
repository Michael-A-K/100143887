# Michael Kongstvedt
# Date of Completion
# Lab Purpose

def periRect(l, w):
    return l*2 + w*2

def trapArea(b1, b2, h):
    return (0.5(b1+b2))

def conicVol(r, h):
    return 0

def cubicBarrier(s):
    return 0

def blastArea(r):
    return 0

def elevationVect(x1, y1, x2, y2):
    return 0

def atmoShift(f):
    return 0

# add more tests to make sure your functions are correctly working
print(periRect(12, 5))
print(periRect(10, 7))
print(periRect(1, 2))
print(periRect(3, 21))

print("{0:.1f}".format(trapArea(3, 3, 3)))

print("{0:.2f}".format(conicVol(4, 4)))

print("{0:.1f}".format(blastArea(7.5)))

print("{0:.2f}".format(elevationVect(1, 9, 14, 2)))

print("{0:.2f}".format(atmoShift(98.6)) + " degrees celsius")
