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
from colored_printing import color_text
from termcolor import colored
import global_stuff
from full_board import full_board
# from getch import getch


class gameboard:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.board = np.full((rows, columns, 2), " "*10)
        # the structure of each element of the 2D matrix of tuples is: {CHAR, TYPE}
        # The upper part
        for i in range(0, 2):
            for j in range(self.columns):
                self.board[i][j][0] = " "
                self.board[i][j][1] = "Top Bar"
        # put the game name
        gamename = "THE MANDALORIAN: THE GAME"
        leng = len(gamename)
        startat = 2  # int(columns/2-leng/2)
        for i in range(leng):
            self.board[0][i+startat][0] = gamename[i]  # put the game name
        # put the score
        scorename = "SCORE: "+str(global_stuff.score).rjust(10, "0")
        leng = len(scorename)
        startat = columns-2-leng
        for i in range(leng):
            self.board[0][i+startat][0] = scorename[i]
        # The game body
        for i in range(2, self.rows-3):
            for j in range(self.columns):
                self.board[i][j][0] = " "
                self.board[i][j][1] = "Normal"
        # the lower part
        for i in range(self.rows-3, self.rows):
            for j in range(self.columns):
                self.board[i][j][0] = " "
                self.board[i][j][1] = "Bottom Bar"

    def print(self):
        # The top menu
        print(Back.BLUE+Fore.WHITE+"", end="")
        for i in range(self.rows):
            for j in range(self.columns):
                # k=self.board[i][j][0]
                # l=self.board[i][j][1]
                # print(self.board[i][j])
                # print(i,j,k,l,self.board[i][j][2])
                # print(colored(self.board[i][j][0],(self.board[i][j][1]),self.board[i][j][2]),end="")
                print(color_text(self.board[i][j]
                                 [0], self.board[i][j][1]), end="")
            print()

    def write_full_on_board(self, full_board, start_in):
        ''' 
        writes the thing from the full board onto the gameboard from the start in to till the screen is completely filled
        '''
        try:
            for i in range(0, full_board.rows):  # all the rows from blahblahblah
                for j in range(0, self.columns):  # all the columns from teh gameboard
                    self.board[i+2][j] = full_board.board[i][j+start_in]
        except Exception as e:
            print(i, j)
            print(full_board.rows, self.columns)
            print(self.board.shape, full_board.board.shape)
            print(e)
            # getch()

    def shift_right(self, full_board, line_to_add):
        '''
        Shift everything to right every .5 seconds
        '''
        # board.shift_right(fb,global_stuff.shown_until)
        for i in range(0, full_board.rows):
            for j in range(0, self.columns-1):
                self.board[i+2][j] = self.board[i+2][j+1]
        for i in range(0, full_board.rows):
            self.board[i+2][self.columns-1] = full_board.board[i][line_to_add]
