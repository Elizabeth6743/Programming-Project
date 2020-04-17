import os
import time
from typing import List

board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
player = 1

Win = 1
Draw = -1
Running = 0
Stop = 1
Game = Running
Mark = 'X'


# Draws Game Board
def draw_board():
    print(" %c| %c | %c " % (board[1], board[2], board[3]))
    print("___|___|___")
    print(" %c | %c | %c " % (board[4], board[5], board[6]))
    print("___|___|___")
    print(" %c | %c | %c " % (board[7], board[8], board[9]))
    print("   |   |   ")


# Checks to see if position is empty or not
def position_check(x):
    if board[x] == ' ':
        return True
    else:
        return False


# Checks to see if player won or not
def Check_Win():
    global Game
    if board[1] == board[2] and board[2] == board[3] and board[1] != ' ':
        Game = Win
    elif board[4] == board[5] and board[5] == board[6] and board[4] != ' ':
        Game = Win
    elif board[7] == board[8] and board[8] == board[9] and board[7] != ' ':
        Game = Win
    elif board[1] == board[4] and board[4] == board[7] and board[1] != ' ':
        Game = Win
    elif board[2] == board[5] and board[5] == board[8] and board[2] != ' ':
        Game = Win
    elif board[3] == board[6] and board[6] == board[9] and board[3] != ' ':
        Game = Win
    # Diagonal Winning Condition
    elif board[1] == board[5] and board[5] == board[9] and board[5] != ' ':
        Game = Win
    elif board[3] == board[5] and board[5] == board[7] and board[5] != ' ':
        Game = Win
    # Match Tie or Draw Conditions
    elif (board[1] != ' ' and board[2] != ' ' and board[3] != ' ' and board[4] != ' ' and board[5] != ' ' and board[
        6] != ' ' and board[7] != ' ' and board[8] != ' ' and board[9] != ' '):
        Game = Draw
    else:
        Game = Running


print('Tic-Tac-Toe Game Designed By Elizabeth Hawkins')

print("Player 1 [X]- Player 2 [O]\n")
print()
print()
print("Please Wait...")
time.sleep(3)
while Game == Running:
    os.system('cls')
    draw_board()
    if player % 2 != 0:
        print("Player 1's turn")
        Mark = 'X'
    else:
        print("Player 2's turn")
        Mark = 'O'
    choice = int(input("Enter a position between [1-9] where you want to mark : "))
    if position_check(choice):
        board[choice] = Mark
        player += 1
        Check_Win()
os.system('cls')
draw_board()
if Game == Draw:
    print("Game Draw")
elif Game == Win:
    player -= 1
    if player % 2 != 0:
        print("Congratulations! Player 1 Won")
    else:
        print("Congratulations! Player 2 Won")
