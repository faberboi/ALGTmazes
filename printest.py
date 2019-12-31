import turtle
x= float(input("Angle: "))
y= float(input("Step: "))
scale = int(input("Scale: "))
window = turtle.Screen()
window.bgcolor("white")
turtle = turtle.Turtle()
turtle.hideturtle()
turtle.color("black")
turtle.speed(100)
turtle.pendown()
size=0
for i in range(scale):
   size+=y
   turtle.left(x)
   turtle.forward(size)

window.exitonclick()