import math
from TurtleWorld import *

world = TurtleWorld()
bob = Turtle()
bob.delay = .01
print (bob)

def shape(t, length, vertices):
    angle = 360 / vertices
    sine = math.sin(math.radians(angle/2))
    side = 2 * length * sine
    beta = (180-angle)/2
    turnangle = beta + angle
    for i in range(vertices):
        rt(t, angle)
        fd(t, length)
        bk(t, length)
    fd(t, length)
    rt(t, turnangle)
    fd(t, side)

       


shape(bob, 150, 7)


wait_for_user()
