import tkinter as tk
import math as math
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

plater_height = 25

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

        elif 400 > pos[0] > 0 and 250 > pos[1] > 247:
            return True
        # inner level walls ^

        else:
            return False

    def rgb_to_hex(r, g, b):
        return '#%02x%02x%02x' %(r, g, b)

    def draw(AllDistances):

        for d in range(0, len(AllDistances)):
            # AllDistances has to have 100 values!!! , also, distance is from 1? to 100
            dist = AllDistances[d]/2
            if dist == 100:
                color = rgb_to_hex(30, 30, 30)
            else:
                color = rgb_to_hex(int(255-dist*2.3), int(255-dist*2.2), int(255-dist*1.1))  # change numbers to rgb
                # 50 * 5.1 ...is the max (to get 255)... 100 * 2.57... is 255.
            canvas.create_rectangle(d*8, 0, (d+1)*8, rooty, fill=color)
            # drawing walls ^

            color = rgb_to_hex(int(250 - dist * 1.1), int(250 - dist * 2.3), int(250 - dist * 2.2))
            canvas.create_rectangle(d*8, rooty-(dist)+plater_height, (d+1)*8, rooty, fill=color)
            # canvas.create_rectangle(d*8, rooty-math.log(dist)*10+plater_height, (d+1)*8, rooty, fill=color)
            # need help to make curve graph into linear, even tho it gives the game a cool vibe xd




        canvas.update()


    def calcDistance(pos, calcangle):
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
                if distance == 200:
                    break
                if in_wall(calcPos.astype(int)):
                    break
            AllDistances.append(distance)

        draw(AllDistances)





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
            calcDistance(location, angle)
        if key.char == 'a':
            if angle == 0:
                angle = 4*np.pi
            angle -= 5*(np.pi/180)  # one degree in radians is 0.01729...
            calcDistance(location, angle)
        if key.char == 's' and not in_wall(location - velocity):
            location = location - velocity
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