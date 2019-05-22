import turtle
def polygon(N:int, a:int):
    turtle.shape('turtle')
    for i in range(N):
        turtle.forward(a)
        turtle.left(360/N)

polygon(int(input()), int(input()))
