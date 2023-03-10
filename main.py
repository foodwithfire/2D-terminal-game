import os, time


def print_game():
    for y in range(w[1]):
        line = ""
        if y == 0 or y == w[1] - 1:
            for x in range(w[0]):
                line += "*"
        else:
            for x in range(w[0]):
                if x == 0 or x == w[0] - 1:
                    line += "*"
                elif x == int(px) and y == int(py):
                    line += "@"
                else:
                    line += " "
        print(line)


px = 17
py = 1
g = 0.1
yvel = 0
w = (35, 10)

while True:
    os.system("cls")

    print_game()

    yvel -= g
    py -= yvel

    if py > w[1] - 2:
        yvel = 1.2

    time.sleep(0.1)
