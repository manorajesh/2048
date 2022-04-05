import keyboard
import random

gameboard = [[0,0,0,0], 
             [0,0,0,0], 
             [0,0,0,0], 
             [0,0,0,0]]

def init():
    print_board()
    add_random()

def add_random():
    global gameboard
    gameboard[random.randint(0,3)][random.randint(0,3)] = 2

def print_board():
    global gameboard
    print('+---+---+---+---+')
    for i in range(4):
        print('|', end='')
        for j in range(4):
            print(gameboard[i][j], end=' ')
        print('|')
    print('+---+---+---+---+')

## Does not work properly
def move(direction):
    global gameboard
    if direction == 'up':
        for i in range(4):
            for j in range(1,4):
                if gameboard[i][j] != 0:
                    for k in range(j-1,-1,-1):
                        if gameboard[i][k] == 0:
                            gameboard[i][k] = gameboard[i][j]
                            gameboard[i][j] = 0
                            break
                        elif gameboard[i][k] == gameboard[i][j]:
                            gameboard[i][k] = gameboard[i][k] + gameboard[i][j]
                            gameboard[i][j] = 0
                            break
    elif direction == 'down':
        for i in range(3,-1,-1):
            for j in range(3,-1,-1):
                if gameboard[i][j] != 0:
                    for k in range(j+1,4):
                        if gameboard[i][k] == 0:
                            gameboard[i][k] = gameboard[i][j]
                            gameboard[i][j] = 0
                            break
                        elif gameboard[i][k] == gameboard[i][j]:
                            gameboard[i][k] = gameboard[i][k] + gameboard[i][j]
                            gameboard[i][j] = 0
                            break
    elif direction == 'left':
        for i in range(4):
            for j in range(1,4):
                if gameboard[j][i] != 0:
                    for k in range(j-1,-1,-1):
                        if gameboard[k][i] == 0:
                            gameboard[k][i] = gameboard[j][i]
                            gameboard[j][i] = 0
                            break
                        elif gameboard[k][i] == gameboard[j][i]:
                            gameboard[k][i] = gameboard[k][i] + gameboard[j][i]
                            gameboard[j][i] = 0
                            break
    elif direction == 'right':
        for i in range(3,-1,-1):
            for j in range(3,-1,-1):
                if gameboard[j][i] != 0:
                    for k in range(j+1,4):
                        if gameboard[k][i] == 0:
                            gameboard[k][i] = gameboard[j][i]
                            gameboard[j][i] = 0
                            break
                        elif gameboard[k][i] == gameboard[j][i]:
                            gameboard[k][i] = gameboard[k][i] + gameboard[j][i]
                            gameboard[j][i] = 0
                            break
    print_board()

init() 
while True:
    keyboard.on_press_key('w', lambda _:move('up'))
    keyboard.on_press_key('s', lambda _:move('down'))
    keyboard.on_press_key('a', lambda _:move('left'))
    keyboard.on_press_key('d', lambda _:move('right'))
    keyboard.unhook_all()
    add_random()