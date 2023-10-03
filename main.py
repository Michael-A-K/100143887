# Michael Kongstvedt
# Date of Completion
# Lab Purpose
import math
def periRect(l, w):
    return l*2 + w*2

def trapArea(b1, b2, h):
    return (0.5*(b1+b2))*h

def conicVol(r, h):
    return (math.pi*(r*r)*(h/3))

def cubicBarrier(s):
    return s*s*s

def blastArea(r):
    return math.pi *(r*r)

def elevationVect(x1, y1, x2, y2):
    return (y2-y1)/(x2-x1)

def atmoShift(f):
    return (f-32)*(5/9)

# add more tests to make sure your functions are correctly working
print("rect1",periRect(12, 5))
print("rect2",periRect(10, 7))
print("rect3",periRect(1, 2))
print("rect4",periRect(3, 21))

print("trap1",trapArea(3, 21, 5))
print("trap2",trapArea(7, 2, 4))
print("trap3",trapArea(1, 9, 3))
print("trap4",trapArea(6, 12, 3))

print("conicVol1",conicVol(3, 12))
print("conicVol2",conicVol(2, 4))
print("conicVol3",conicVol(5, 8))
print("conicVol4",conicVol(9, 7))

print("Cube1",cubicBarrier(3))
print("Cube2",cubicBarrier(15))
print("Cube3",cubicBarrier(8))
print("Cube4",cubicBarrier(7))

print("CircleA1",blastArea(3))
print("CircleA2",blastArea(5))
print("CircleA3",blastArea(11))
print("CircleA4",blastArea(24))

print("elevationVect1",elevationVect(3, 7, 12, 5))
print("elevationVect2",elevationVect(4, 5, 9, 6))
print("elevationVect3",elevationVect(0, 1, 13, 15))
print("elevationVect4",elevationVect(30, 27, 0, 2))

print("{0:.1f}".format(trapArea(3, 3, 3)))

print("{0:.3f}".format(cubicBarrier(6)))

print("{0:.2f}".format(conicVol(4, 4)))

print("{0:.1f}".format(blastArea(7.5)))

print("{0:.2f}".format(elevationVect(1, 9, 14, 2)))

print("{0:.2f}".format(atmoShift(98.6)) + " degrees celsius")
