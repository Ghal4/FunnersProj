import tkinter as tk

import numpy
import numpy as np

root = tk.Tk()
rootx = 800
rooty = 500
root.geometry(f'{rootx}x{rooty}')
root.resizable(width=False, height=False)

CharacterXY = [2, 2]

canvas = tk.Canvas(root, width=rootx, height=rooty)
canvas.pack(anchor='nw')
canvas.configure(bg='black', borderwidth=0, highlightthickness=0)
canvas.update()

location = np.array([50, 50])
angle = 0


def makewalls():
    a, b, c, d = 0, 0, 0, 0
    walls = []
    for i in range(0, rootx*2+rooty*2):
        if i < rootx:
            a += 1
            walls.append(f'{a},{5}')
        elif i < rootx*2:
            b += 1
            walls.append(f'{b},{rooty}')
        elif i < rootx*2+rooty:
            c += 1
            walls.append(f'{0},{c}')
        else:
            d += 1
            walls.append(f'{rootx},{d}')

    return walls


WallsPos = makewalls()
WallsPos.append('here ends the outer layer walls')


def draw(pos, size, color):
    canvas.create_rectangle(pos[0], pos[1], pos[0]+size, pos[1]+size, fill=color)
    canvas.update()


AllDistances = []
def calcDistance(pos, calcangle):
    global AllDistances
    AllDistances = []
    for a in range(0, 100):  # how do I make this function to stop working after it has been called again?
        distance = 0
        p = 1  # magnitude??
        vx = p * (np.cos(calcangle-(50-a)*0.0174533))
        vy = p * (np.sin(calcangle-(50-a)*0.0174533))
        velocity = np.array([vx, vy])
        calcPos = pos

        while(True):
            calcPos = calcPos + velocity
            distance += 1
            if distance == 100:
                break
            if f'{calcPos[0]},{calcPos[1]}' in WallsPos:
                break
        AllDistances.append(distance)
        draw(calcPos, 3, 'red')





def jump():
    aaaaa = "aaaaaaaaaaaaaaaaaaaaaaaaa"


def keydown(key):
    global CharacterXY
    global CharacterAngle
    global location
    global angle

    p = 1  # magnitude of the vector. idk what is this lol
    vx = p*(np.cos(angle))
    vy = p*(np.sin(angle))
    velocity = np.array([vx*5, vy*5])


    if key.char == 'w':
        location = location + velocity
        draw(location, 10, 'white')
        calcDistance(location, angle)
    if key.char == 'a':
        if angle == 0:
            angle = 4*numpy.pi
        angle -= 5*0.0174533  # one degree in radians is 0.01...
        calcDistance(location, angle)
    if key.char == 's':
        location = location - velocity
        draw(location, 10, 'white')
        calcDistance(location, angle)
    if key.char == 'd':
        if angle == 4*numpy.pi:
            angle = 0
        angle += 5*0.0174533  # one degree in radians
        calcDistance(location, angle)
    if key.char == 'space':
        jump

    # 20 times pressing D or A is 90 degrees


root.bind("<KeyPress>", keydown)


root.mainloop()