import turtle
def polygon(N:int, a:int):
    for i in range(N):
        turtle.forward(a)
        turtle.left(90)
        turtle.forward(a)
        turtle.left(90)
        turtle.forward(a)
        turtle.left(90)
        turtle.forward(a)
        turtle.left(90)
        turtle.penup()
        turtle.backward(10)
        turtle.right(90)
        turtle.forward(10)
        turtle.left(90)
        turtle.pendown()
        a += 20

polygon(int(input()), int(input()))

