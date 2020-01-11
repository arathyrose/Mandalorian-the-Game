'''
The person class: 

This is a base class for the charcters in the game  

He has the following attributes:

- x position on the screen
- y position on the screen
- height
- width
- character for filling him/her/it

and the following functions:

- initialize itself
- render itself to the screen
- kill itself
'''
from gameboard import gameboard


class person:
    def __init__(self, x, y, h, w, style):
        self.x = x
        self.y = y
        self.h = h
        self.w = w
        self.style = style
        self.pointed = "LEFT"

    def write_self_on_board(self, gameboard):
        for i in range(self.h):
            for j in range(self.w):
                gameboard.board[i+self.x][j+self.y] = self.style[i][j]

    def kill_self(self, gameboard):
        for i in range(self.h):
            for j in range(self.w):
                gameboard.board[i+self.x][j+self.y] = " "
