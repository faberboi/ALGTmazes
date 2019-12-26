from tkinter import PhotoImage # for scaling the background image (maze)
import turtle as t
from matplotlib.image import imread

filename = './Mazes/Mini11.png'

def PathFinder(startPos):
    maze = imread(filename)[::-1]
    mazeLayout = [len(maze), len(maze[1])]
    if maze[startPos[0], startPos[1]] == 0:
        print("Look for the walls")
        return 0

    t.mode('logo') # setting default orientation north - Ruppi2D2's favorite ;-)

    screen = t.Screen()
    screen.setup(width = 1000, height = 512)
    screen.bgcolor('gray')
    zoom=14
    bgMaze = PhotoImage(file=filename).zoom(zoom,zoom) # change to automatic scaling s.t. it fills window!
    screen.addshape('bgMaze', t.Shape('image', bgMaze))

    biggy = t.Turtle('bgMaze')
    biggy.stamp()
    biggy.hideturtle()

    turtle = t.Turtle('classic')
    turtle.color('green')
    turtle.pensize(7)
    turtle.hideturtle()
    turtle.turtlesize(stretch_wid=5, stretch_len=5, outline=None)
    turtle.penup()
    turtle.speed(0)
    if startPos[0] > 13:
        turtle.right(90)
        turtle.forward((startPos[0] - mazeLayout[0]//2)*zoom)
        turtle.left(90)
    elif startPos[0] < 13:
        turtle.left(90)
        turtle.forward(abs(startPos[0] - mazeLayout[0]//2) * zoom)
        turtle.right(90)
    if startPos[1] > 13:
        turtle.forward((startPos[0] - mazeLayout[1]//2) * zoom)
    elif startPos[0] < 13:
        turtle.left(180)
        turtle.forward(abs(startPos[0] - mazeLayout[1]//2) * zoom)
        turtle.right(180)
    for k in range(34):
        turtle.pendown()
        turtle.forward(zoom)
        turtle.right(90)
        turtle.forward(zoom)
        turtle.left(90)

    screen.exitonclick()
    t.TurtleScreen._RUNNING = True # otherwise redoing would throw a Terminator-error

PathFinder([4,4])

