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

location = np.array([400, 400])
angle = 0


def startgame():
    def in_wall(pos):
        if pos[0] < 0+1:
            return True
        elif pos[0] > rootx-1:
            return True
        elif pos[1] < 0 + 1:
            return True
        elif pos[1] > rooty - 1:
            return True
        # outer level walls ^

        elif 199 > pos[0] > 99 and 103 > pos[1] > 99:
            return True
        elif 199 > pos[0] > 196 and 199 > pos[1] > 99:
            return True
        elif 199 > pos[0] > 99 and 199 > pos[1] > 196:
            return True

        # inner level walls ^

        else:
            return False


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
            vx = p * (np.cos(calcangle-(50-a)*(np.pi/180)))
            vy = p * (np.sin(calcangle-(50-a)*(np.pi/180)))
            velocity = np.array([vx, vy])
            calcPos = pos

            while(True):
                calcPos = calcPos + velocity
                distance += 1
                if distance == 100:
                    break
                if in_wall(calcPos.astype(int)):
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


        if key.char == 'w' and not in_wall(location + velocity):
            location = location + velocity
            draw(location, 10, 'white')
            calcDistance(location, angle)
        if key.char == 'a':
            if angle == 0:
                angle = 4*np.pi
            angle -= 5*(np.pi/180)  # one degree in radians is 0.01729...
            calcDistance(location, angle)
        if key.char == 's' and not in_wall(location - velocity):
            location = location - velocity
            draw(location, 10, 'white')
            calcDistance(location, angle)
        if key.char == 'd':
            if angle == 4*np.pi:
                angle = 0
            angle += 5*(np.pi/180)  # one degree in radians
            calcDistance(location, angle)
        if key.char == 'space':
            jump

        # 18 times pressing D or A is 90 degrees

    root.bind("<KeyPress>", keydown)

#make level here, set walls.

# start game
startgame()

root.mainloop()