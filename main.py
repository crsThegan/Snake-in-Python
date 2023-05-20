import os
import keyboard
import random

width, height = 50, 20
board = []
score = 0
game_over = False

snakeX, snakeY = [width // 2], [height // 2]
snake_dir = 'right'
prevX, prevY = 0, 0

fruitX, fruitY = random.randint(1, width - 2), random.randint(1, height - 2)

def setup():
    for x in range(width):
        board.append([])
        for y in range(height):
            if x == 0 or x == width - 1 or y == 0 or y == height - 1:
                board[x].append('#')
            else:
                board[x].append(' ')

def changeBoard():
    for x in range(1, width - 1):
        for y in range(1, height - 1):
            board[x][y] = ' '
            board[fruitX][fruitY] = 'F'
            for i in range(len(snakeX)):
                if x == snakeX[i] and y == snakeY[i]:
                    board[x][y] = 'O' if i == 0 else 'o'

def draw():
    for y in range(height - 1, -1, -1):
        for x in range(width):
            print(board[x][y], end='')
            
        if y == height // 2 + 1:
            print(f"       Score: {score}")
        elif y == height // 2 and game_over == True:
            print("       Game over!")
        else:
            print()

def logics():
    global prevX, prevY
    global fruitX, fruitY
    global score
    global game_over
    prevX, prevY = snakeX[-1], snakeY[-1]
    for i in range(len(snakeX) - 1, 0, -1):
        snakeX[i] = snakeX[i - 1]
        snakeY[i] = snakeY[i - 1]
    
    if snake_dir == 'right':
        snakeX[0] += 1
    elif snake_dir == 'left':
        snakeX[0] -= 1
    elif snake_dir == 'up':
        snakeY[0] += 1
    elif snake_dir == 'down':
        snakeY[0] -= 1
    
    if snakeX[0] == width - 1:
        snakeX[0] = 1
    elif snakeX[0] == 0:
        snakeX[0] = width - 2
    elif snakeY[0] == height - 1:
       snakeY[0] = 1
    elif snakeY[0] == 0:
        snakeY[0] = height - 2
    
    if snakeX[0] == fruitX and snakeY[0] == fruitY:
        score += 5
        snakeX.append(prevX)
        snakeY.append(prevY)
        changeBoard()
        while board[fruitX][fruitY] != ' ':
            fruitX, fruitY = random.randint(1, width - 2), random.randint(1, height - 2)
    
    for i in range(1, len(snakeX)):
        if snakeX[0] == snakeX[i] and snakeY[0] == snakeY[i]:
            game_over = True

def action_check():
    global snake_dir
    if keyboard.is_pressed('d'):
        snake_dir = 'right'
    elif keyboard.is_pressed('a'):
        snake_dir = 'left'
    elif keyboard.is_pressed('w'):
        snake_dir = 'up'
    elif keyboard.is_pressed('s'):
        snake_dir = 'down'
        

setup()
draw()
while not game_over:
    action_check()
    logics()
    changeBoard()
    draw()
    os.system("cls")

draw()