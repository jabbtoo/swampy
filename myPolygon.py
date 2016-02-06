import math

from TurtleWorld import *

world = TurtleWorld()
bob = Turtle()
bob.delay = .05 
print (bob)



def hexagon(t, length):
    
        for i in range(6):
            fd(t, length)
            rt(t, 60)

hexagon(bob, 100)



wait_for_user()
