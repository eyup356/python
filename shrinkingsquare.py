import turtle

turtle_screen=turtle.Screen()
turtle_screen.bgcolor("light green")
turtle_screen.title("turtle pyrthon")

turtle_instance = turtle.Turtle()
turtle_instance.color("blue")
def shrinkingSquare(size):
    for i in range(4):
        turtle_instance.forward(size)
        turtle_instance.left(90)
        size = size - 5

x = int(200)
while x > 0:
    shrinkingSquare(x)

    x=x - 20

turtle.done()