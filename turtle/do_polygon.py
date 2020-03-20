import turtle
import random



def do_polygon(size, side):
    colors = ( 'blue', 'green', 'red', 'red', 'pink', 'magenta', 'purple', 'gray', 'yellow' )
    angle = 360 / side
    for i in range(side):
        turtle.color(random.choice(colors)) #picks color randomly for each side
        turtle.fd(size)
        turtle.lt(angle)


do_polygon(100, 8)