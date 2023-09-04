import turtle
drawing_board=turtle.Screen()
drawing_board.bgcolor("yellow")
drawing_board.title("Python Turtle Test")
turtle_instance=turtle.Turtle()
'''
def turtle_ciz():
    for x in range(4):
        turtle_instance.forward(100)
        turtle_instance.left(90)

turtle_ciz()
'''
def star_draw():
    for x in range(10):
        turtle_instance.forward(100)
        turtle_instance.right(36)

star_draw()
'''
turtle_instance_2=turtle.Turtle()
turtle_instance_2.forward(30)
turtle_instance_2.left(180)
turtle_instance_2.forward(450)
'''
turtle.done()
