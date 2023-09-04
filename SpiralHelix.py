import turtle
turtle_screen=turtle.Screen()
turtle_screen.bgcolor("black")
turtle_screen.title("turtle pyrthon")
turtle_instance = turtle.Turtle()
turtle_instance.color("blue")
turtle_colors=["red","blue","yellow","green","orange","purple"]

for i in range(10):
    turtle_instance.color(turtle_colors[i%6])
    turtle_instance.circle(10*i)
    turtle_instance.circle(-10*i)
    turtle_instance.left(i)
turtle.mainloop()
#turtle.done()