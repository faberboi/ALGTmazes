from tkinter import PhotoImage # for scaling the background image (maze)
import turtle as tur
from matplotlib.image import imread

'''
---------PathFinder-------------
'''

def findPath(startPos):
    maze = imread(filename)[::-1]
    mazeLayout = [len(maze), len(maze[1])]
    print(mazeLayout)
    distance = 0
    angle = 0
    if maze[startPos[1], startPos[0]] == 0:
        print("Look for the walls")
        return 0

    t.penup()
    t.speed(0)

    '''
    ---------Go to Start-------------
    '''
    if startPos[0] > mazeLayout[0]//2:
        t.right(90); angle += 90
        t.forward((startPos[0] - mazeLayout[1]//2)*zoom)
        t.left(90); angle -= 90
    elif startPos[0] < mazeLayout[0]//2:
        t.left(90); angle -= 90
        t.forward(abs(startPos[0] - mazeLayout[1]//2) * zoom)
        t.right(90); angle += 90
    if startPos[1] > mazeLayout[1]//2:
        t.forward((startPos[1] - mazeLayout[0]//2) * zoom)
    elif startPos[1] < mazeLayout[1]//2:
        t.left(180); angle -= 180
        t.forward(abs(startPos[1] - mazeLayout[0]//2) * zoom)
        t.right(180); angle += 180

    t.pendown()
    pos = startPos
    front = maze[pos[1]+1, pos[0]]

    pos, distance, angle, left, front = goForward(pos, distance, maze, front)



    while pos[1] >= 5:
        while left != 1 and front != 0:
            t.forward(zoom)
            distance += 1
            if angle % 360 == 0:
                pos[1] += 1
                left = maze[pos[1], pos[0] - 1]
                front = maze[pos[1]+1, pos[0]]
            elif angle % 360 == 90:
                pos[0] += 1
                left = maze[pos[1] + 1, pos[0]]
                front = maze[pos[1], pos[0] + 1]
            elif angle % 360 == 180:
                pos[1] -= 1
                left = maze[pos[1], pos[0] + 1]
                front = maze[pos[1]-1, pos[0]]
            elif angle % 360 ==270:
                pos[0] -= 1
                left = maze[pos[1] - 1, pos[0]]
                front = maze[pos[1], pos[0] - 1]

        if pos[1] < 5:
            print(distance)
            break

        if left == 1:
            t.left(90); angle -= 90
            if angle % 360 == 0:
                pos, distance, angle, left, front = goForward(pos, distance, maze, front)
                continue
            else:
                t.forward(zoom)
                distance += 1
        elif front == 0:
            t.right(90); angle += 90
            if angle % 360 == 0:
                pos, distance, angle, left, front = goForward(pos, distance, maze, front)
            elif angle % 360 == 90:
                front = maze[pos[1], pos[0]+1]
            elif angle % 360 == 180:
                front = maze[pos[1]-1, pos[0]]
            elif angle % 360 == 270:
                front = maze[pos[1], pos[0]-1]
            continue
        if angle % 360 == 90:
            pos[0] += 1
            left = maze[pos[1] + 1, pos[0]]
            front = maze[pos[1], pos[0] + 1]
        elif angle % 360 == 180:
            pos[1] -= 1
            left = maze[pos[1], pos[0] + 1]
            front = maze[pos[1]-1, pos[0]]
        elif angle % 360 == 270:
            pos[0] -= 1
            left = maze[pos[1] - 1, pos[0]]
            front = maze[pos[1], pos[0] - 1]




    screen.exitonclick()
    tur.TurtleScreen._RUNNING = True # otherwise redoing would throw a Terminator-error

def goForward(pos, distance, maze, front):
    angle = 0
    front = maze[pos[1], pos[0] + 1]
    while front != 0:
        pos[1] += 1
        t.forward(zoom)
        distance += 1
        front = maze[pos[1] + 1, pos[0]]

    t.right(90); angle += 90
    left = front
    front = maze[pos[1], pos[0]+1]
    return pos, distance, angle, left, front

'''
--------------main-----------------
'''
filename = './Mazes/Mini10.png'

tur.mode('logo') # setting default orientation north - Ruppi2D2's favorite ;-)

screen = tur.Screen()
screen.setup(width = 1300, height = 700)
screen.bgcolor('gray')
zoom=20
bgMaze = PhotoImage(file=filename).zoom(zoom,zoom) # change to automatic scaling s.t. it fills window!
screen.addshape('bgMaze', tur.Shape('image', bgMaze))

biggy = tur.Turtle('bgMaze')
biggy.stamp()
biggy.hideturtle()

t = tur.Turtle('classic')
t.color('green')
t.pensize(3)
#t.hideturtle()
t.turtlesize(stretch_wid=2, stretch_len=2, outline=None)
findPath([12,6])

#good positions
#labyrint01 12,20
