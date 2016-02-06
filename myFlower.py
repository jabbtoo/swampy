import math
from TurtleWorld import *

world = TurtleWorld()
bob = Turtle()
bob.delay = .01

print (bob)


def polyline(t, n, length, angle):
    for i in range(n):
        fd(t, length)
        lt(t, angle)

def arc(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n
    polyline(t, n, step_length, step_angle)

arc(bob, 500, 20)
lt(bob, 160)
arc(bob, 500, 20)
rt(bob, 180)
wait_for_user()
