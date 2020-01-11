'''
Contains the initialization of the game board
has the following components:

rows: height of the board   : Here I fix it as 50
columns: width of the board : Here I fix it as 200

The rows can be divided into the following parts
0 -> 2: The top bar that contains the name of the game colored with blue
rows-3 -> rows: the bottom bar containing the lives left and the time remaining
'''
import numpy as np
from colorama import Fore, Back, Style


class gameboard:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.board = np.full((rows, columns), " ")
        gamename = "THE MANDALORIAN"
        leng = len(gamename)
        startat = int(columns/2-leng/2)
        for i in range(leng):
            self.board[0][i+startat] = (gamename[i])

    def print(self):
        # The top menu
        print(Back.BLUE+Fore.WHITE+"", end="")
        for i in range(0, 2):
            for j in range(self.columns):
                print(self.board[i][j], end="")
            print()
        # The main game
        print(Style.RESET_ALL+"", end="")
        for i in range(1, self.rows-3):
            for j in range(self.columns):
                print(self.board[i][j], end="")
            print()
        # The bottom thing
        print(Back.BLUE+Fore.WHITE+"", end="")
        for i in range(self.rows-3, self.rows):
            for j in range(self.columns):
                print(self.board[i][j], end="")
            print()
        print(Style.RESET_ALL+" ")
