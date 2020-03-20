import turtle

def do_square(size, color):
    turtle.color(color)
    for i in range(4):
        turtle.fd(size)
        turtle.lt(90)
do_square(250, 'blue')