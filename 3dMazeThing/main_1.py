import tkinter as tk

root = tk.Tk()
rootx = 800
rooty = 500
root.geometry(f'{rootx}x{rooty}')
root.resizable(width=False, height=False)

CharacterXY = [2, 2]
AngleXY = ['90 degrees', '90 degrees']

canvas = tk.Canvas(root, width=rootx, height=rooty)
canvas.pack(anchor='nw')
canvas.configure(bg='black', borderwidth=0, highlightthickness=0)
canvas.update()

CharacterAngle = 90

def makewalls():
    a, b, c, d = 0,0,0,0
    walls = []
    for i in range(0, rootx*2+rooty*2):
        if i < rootx:
            a += 1
            walls.append(f'{a},{0}')
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

def calculateXYtoAdd(angle):
    XY_to_add = [0, 0]
    if angle == 90:
        XY_to_add = [0, 90]
    if angle == 180:
        XY_to_add = [90, 0]
    if angle == 270:
        XY_to_add = [0, -90]
    if angle == 360:
        XY_to_add = [-90, 0]

    if 0 < angle < 90:
        XY_to_add = [angle-90, -90]
    if 90 < angle < 180:
        XY_to_add = [angle-90, 90]
    if 180 < angle < 270:
        XY_to_add = [90, angle-90]
    if 270 < angle < 360:
        XY_to_add = [-90, angle-90]

    XY_to_add[0] = XY_to_add[0]/90
    XY_to_add[1] = XY_to_add[1] / 90
    return XY_to_add

def draw(pos):
    canvas.create_rectangle(pos[0], pos[1], pos[0]+10, pos[1]+10, fill='white')
    canvas.update()


AllDistances = []
def calcDistance(pos, direction):
    global AllDistances
    AllDistances = []
    calcPos = [0, 0]
    calcAngle = (direction - 50)
    distance = 0
    for a in range(0, 100):
        XY_add_calc = calculateXYtoAdd(calcAngle)
        distance = 0
        calcPos = CharacterXY

        while(True):
            calcPos[0] += XY_add_calc[0]
            calcPos[1] += XY_add_calc[1]
            distance += 1
            if distance == 100:
                something = 1
            if f'{calcPos[0]},{calcPos[1]}' in WallsPos:
                something = 1
            else:
                break

        AllDistances.append(distance)
        calcAngle += a




def jump():
    aaaaa = "aaaaaaaaaaaaaaaaaaaaaaaaa"




def keydown(key):
    global CharacterXY
    global CharacterAngle

    if key.char == 'w':
        CharacterXY[1] -= 5
        add = calculateXYtoAdd(CharacterAngle)
        CharacterXY[0] += add[0]
        CharacterXY[1] += add[1]
        draw(CharacterXY)
        #calcDistance(CharacterXY[0], CharacterXY[1])
    if key.char == 'a':
        CharacterAngle -= 1
        #calcDistance(CharacterXY[0], CharacterXY[1])
    if key.char == 's':
        CharacterXY[1] += 5
        add = calculateXYtoAdd(CharacterAngle)
        CharacterXY[0] += add[0]
        CharacterXY[1] += add[1]
        draw(CharacterXY)
        #calcDistance(CharacterXY[0], CharacterXY[1])
    if key.char == 'd':
        CharacterAngle += 1
        #calcDistance(CharacterXY[0], CharacterXY[1])
    if key.char == 'space':
        jump

root.bind("<KeyPress>", keydown)


root.mainloop()