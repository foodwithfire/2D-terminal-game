import os, sys, time
try:
    import keyboard
except:
    print("Error : Can't import keyboard.\n Please download the 'keyboard' module --> Enter 'pip install keyboard' in the terminal.")
    sys.exit()


# Player position
px = 17
py = 1

pdir = (0, 0)

# Size of the windows
w = (35, 10)

# Game loop
while True:

    # Clear console

    try:
        # windows
        os.system("cls")
    except:
        # linux
        os.system("clear")

    # Print the screen

    for y in range(w[1]):
        line = ""
        if y == 0 or y == w[1] - 1:
            for x in range(w[0]):
                line += "-"
        else:
            for x in range(w[0]):
                if x == 0 or x == w[0] - 1:
                    line += "|"
                elif x == int(px) and y == int(py):
                    line += "#"
                else:
                    line += " "
        print(line)

    # Movements

    pdir = [0, 0]
    print("Press [z], [q], [s] or [d] to move.")

    pdir[0] = keyboard.is_pressed("d") - keyboard.is_pressed("q")
    pdir[1] = keyboard.is_pressed("s") - keyboard.is_pressed("z")

    px += pdir[0]
    py += pdir[1]

    # Collisions

    if px < 1:
        px = 1
    if px > w[0] - 2:
        px = w[0] - 2
    if py < 1:
        py = 1
    if py > w[1] - 2:
        py = w[1] - 2

    # 0.1s pause

    time.sleep(0.1)
