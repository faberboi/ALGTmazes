from tkinter import PhotoImage # for scaling the background image (maze)
import turtle as tur
from matplotlib.image import imread

filename = './Mazes/Mini11.png'

def PathFinder(startPos):
    maze = imread(filename)[::-1]
    distance = 0
    mazeLayout = [len(maze), len(maze[1])]
    if maze[startPos[1], startPos[0]] == 0:
        print("Look for the walls")
        return 0

    tur.mode('logo') # setting default orientation north - Ruppi2D2's favorite ;-)

    screen = tur.Screen()
    screen.setup(width = 1000, height = 512)
    screen.bgcolor('gray')
    zoom=14
    bgMaze = PhotoImage(file=filename).zoom(zoom,zoom) # change to automatic scaling s.t. it fills window!
    screen.addshape('bgMaze', tur.Shape('image', bgMaze))

    biggy = tur.Turtle('bgMaze')
    biggy.stamp()
    biggy.hideturtle()

    t = tur.Turtle('classic')
    t.color('green')
    t.pensize(7)
    #t.hideturtle()
    t.turtlesize(stretch_wid=2, stretch_len=2, outline=None)
    t.penup()
    t.speed(0)
    if startPos[0] > mazeLayout[0]//2:
        t.right(90)
        t.forward((startPos[0] - mazeLayout[0]//2)*zoom)
        t.left(90)
    elif startPos[0] < mazeLayout[0]//2:
        t.left(90)
        t.forward(abs(startPos[0] - mazeLayout[0]//2) * zoom)
        t.right(90)
    if startPos[1] > mazeLayout[1]//2:
        t.forward((startPos[1] - mazeLayout[1]//2) * zoom)
    elif startPos[1] < mazeLayout[1]//2:
        t.left(180)
        t.forward(abs(startPos[1] - mazeLayout[1]//2) * zoom)
        t.right(180)

    t.pendown()
    t.speed(2)
    pos = startPos
    front = maze[pos[1]+1, pos[0]]
    #find Wall
    while front != 0:
        pos[1] += 1
        t.forward(zoom)
        distance += 1
        front = maze[pos[1] + 1, pos[0]]

    t.right(90)
    left = front
    front = maze[pos[1], pos[0]+1]



    while pos[1] >= 5:
        while left != 1 and front != 0:
            dir = t.heading()
            t.forward(zoom)
            distance += 1
            if dir == 0:
                pos[1] += 1
                left = maze[pos[1], pos[0] - 1]
                front = maze[pos[1]+1, pos[0]]
            elif dir == 90:
                pos[0] += 1
                left = maze[pos[1] + 1, pos[0]]
                front = maze[pos[1], pos[0] + 1]
            elif dir == 180:
                pos[1] -= 1
                left = maze[pos[1], pos[0] + 1]
                front = maze[pos[1]-1, pos[0]]
            elif dir ==270:
                pos[0] -= 1
                left = maze[pos[1] - 1, pos[0]]
                front = maze[pos[1], pos[0] - 1]

        if pos[1] < 5:
            print(distance)
            break

        if left == 1:
            t.left(90)
            t.forward(zoom)
            distance += 1
        elif front == 0:
            t.right(90)
            front = 1
            continue
        dir = t.heading()
        if dir == 0:
            pos[1] += 1
            left = maze[pos[0] - 1, pos[1]]
        elif dir == 90:
            pos[0] += 1
            left = maze[pos[0], pos[1] + 1]
        elif dir == 180:
            pos[1] -= 1
            left = maze[pos[0] + 1, pos[1]]
        elif dir == 270:
            pos[0] -= 1
            left = maze[pos[0], pos[1] - 1]




    screen.exitonclick()
    tur.TurtleScreen._RUNNING = True # otherwise redoing would throw a Terminator-error

PathFinder([11,11])

