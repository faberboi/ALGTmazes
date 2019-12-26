from tkinter import PhotoImage # for scaling the background image (maze)
import turtle as t
from matplotlib.image import imread

filename = './Mazes/Mini11.png'

def PathFinder(startPos):
    maze = imread(filename)[::-1]
    if maze[startPos[0], startPos[1]] == 0:
        print("Look for the walls")
        return 0

    t.mode('logo') # setting default orientation north - Ruppi2D2's favorite ;-)

    screen = t.Screen()
    screen.setup(width = 1000, height = 512)
    screen.bgcolor('gray')
    bgMaze = PhotoImage(file=filename).zoom(20, 20) # change to automatic scaling s.t. it fills window!
    screen.addshape('bgMaze', t.Shape('image', bgMaze))

    biggy = t.Turtle('bgMaze')
    biggy.stamp()
    biggy.hideturtle()

    turtle = t.Turtle('classic')
    turtle.color('green')
    turtle.pensize(10)
    turtle.hideturtle()
    turtle.turtlesize(stretch_wid=5, stretch_len=5, outline=None)
    turtle.penup()
    turtle.speed(0)
    if startPos[0] > 13:
        turtle.right(90)
        turtle.forward((startPos[0]-12)*20)
        turtle.left(90)
    elif startPos[0] < 13:
        turtle.left(90)
        turtle.forward(abs(startPos[0] - 12) * 20)
        turtle.right(90)
    if startPos[1] > 13:
        turtle.forward((startPos[0] - 12) * 20)
    elif startPos[0] < 13:
        turtle.left(180)
        turtle.forward(abs(startPos[0] - 12) * 20)
        turtle.right(180)
    turtle.pendown()
    turtle.forward(100)

    screen.exitonclick()
    t.TurtleScreen._RUNNING = True # otherwise redoing would throw a Terminator-error

PathFinder([0,0])

