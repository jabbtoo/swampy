from TurtleWorld import *

world = TurtleWorld()
bob = Turtle()
print (bob)



def star(t, length, vertices):
    angle = (360 / vertices)
    for i in range(vertices):
            fd(t, length)
            rt(t, angle)

            for x in range(vertices / 3):
                fd(t, length)
                rt(t, angle * 2)

def pentagon(t, length, vertices):
    angle = 360/vertices
    lt(t, 180-angle)
    for i in range(vertices):
        rt(t, angle)
        fd(t, length)

star(bob, 75, 7)
pentagon(bob, 75, 7)


wait_for_user()
