# Imports
import sys, time, os
from random import randint
os.system("")
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
signs = []
signs.append(20)
signs.append(5)
signs.append("Hello world")

for i in range(randint(int((w[0]*w[1])/160), int((w[0]*w[1])/20))):
    x = px
    while x == px:
        x = randint(1, w[0] - 2)
    obs.append(x)

    y = py
    while y == py:
        y = randint(1, w[1] - 2)
    obs.append(y)

    for i in range(randint(1, 4)):
        x += randint(-1, 1)
        y += randint(-1, 1)
        while x <= 2 or x > w[0 - 2]:
            x += randint(-1, 1)
        while y <= 2 or y > w[1 - 2]:
            y += randint(-1, 1)
        obs.append(x)
        obs.append(y)


code = {
    " ": 10, "\n": 11, "╔": 12, "╗": 13, "╚": 14, "╝": 15, "═": 16, "║": 17, "@": 18, "#": 19, "?": 20, "◯": 21
}


def genworld():
    screen = ""

    for y in range(w[1]):
        line = ""
        if y == 0:
            line += "╔═" + "═" * (w[0] - 4) + "═╗"

        elif y == w[1] - 1:
            line += "╚═" + "═" * (w[0] - 4) + "═╝"
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

                idx = 0
                for i in range(int(len(signs) / 3)):
                    if x == signs[idx] and y == signs[idx + 1]:
                        temp = list(line)
                        temp[x - 1] = "?"
                        line = ""
                        for letter in temp:
                            line += letter
                    idx += 3

                if x == 0 or x == w[0] - 1:
                    # Walls
                    line += "║"
                elif x == int(px) and y == int(py):
                    # Player
                    line += "◯"
                else:
                    line += " "
        screen += line + "\n"
    return screen


def encodegen(g):
    seed = ""
    for char in g:
        seed += str(code[char])
    return seed


def decodeseed(seed):
    screen = ""
    idx = 0
    for i in range(int(len(seed)/2)):
        screen += list(code.keys())[list(code.values()).index(int(str(seed[idx] + str(seed[idx + 1]))))]
        idx += 2
    return screen

# Update method
def update():
    # print window
    print(f"\033[0;0H{decodeseed(encodegen(genworld()))}\nPress [z], [q], [s] or [d] to move.\nx: {px}  |  y: {py}")


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
    update()
