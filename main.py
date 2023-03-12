import sys
import time
from os import system
from random import randint

try:
    import keyboard
except:
    print("Error : Can't import keyboard.\n Please download the 'keyboard' module --> Enter 'pip install keyboard' in the terminal.\nNote : this will only work if you're using an IDE (like PyCharm for example).")
    sys.exit()


# Size of the windows
w = (80, 20)

# Player position
px = int(w[0] / 2)
py = int(w[1] / 2)

pdir = (0, 0)

# Obstacles position
obs = []

for i in range(randint(1, 100)):
    x = px
    while x == px:
        x = randint(1, w[0] - 2)
    obs.append(x)
    y = py
    while y == py:
        y = randint(1, w[1] - 2)
    obs.append(y)


# Update method
def update():
    # print window
    for y in range(w[1]):
        line = ""
        if y == 0 or y == w[1] - 1:
            for x in range(w[0]):
                # Walls
                line += "-"
        else:
            for x in range(w[0]):
                idx = 0
                for i in range(int(len(obs) / 2)):
                    if x == obs[idx] and y == obs[idx + 1]:
                        # Obstacles
                        temp = list(line)
                        temp[x - 1] = "#"
                        line = ""
                        for letter in temp:
                            line += letter
                    idx += 2
                if x == 0 or x == w[0] - 1:
                    # Walls
                    line += "|"
                elif x == int(px) and y == int(py):
                    # Player
                    line += "@"
                else:
                    line += " "
        print(line)
    print("Press [z], [q], [s] or [d] to move.")
    print(f"x: {px}  |  y: {py}")


# Check wall collisions
def wallcollision():
    global px
    global py

    if px < 1:
        px = 1
    if px > w[0] - 2:
        px = w[0] - 2
    if py < 1:
        py = 1
    if py > w[1] - 2:
        py = w[1] - 2


# Game loop
oldpx = 0
oldpy = 0
update()
while True:

    # Movements
    pdir = [0, 0]
    pdir[0] = keyboard.is_pressed("d") - keyboard.is_pressed("q")
    pdir[1] = keyboard.is_pressed("s") - keyboard.is_pressed("z")

    px += pdir[0]
    py += pdir[1]

    # Collisions
    wallcollision()

    idx = 0
    for i in range(int(len(obs) / 2)):
        if obs[idx] - 1 == px and obs[idx + 1] == py:
            px = oldpx
            py = oldpy
            pdir = [0, 0]
        idx += 2

    if not pdir[0] == 0 or not pdir[1] == 0:
        update()

    oldpx = px
    oldpy = py

    # 0.05s pause
    time.sleep(0.05)
