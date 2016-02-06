from TurtleWorld import *

world = TurtleWorld()
bob = Turtle()
print (bob)
bob.delay = .0001


def polygon(t, n, length):
    angle= 360.0 / n
    for i in range(n):
        fd(t, length)
        lt(t, angle)

def circle(t, r):
    circum = 6.28 * r
    n = int(circum / 3) + 1
    length = circum / n
    polygon(t, n, length)

circle(bob, 200)

wait_for_user()
