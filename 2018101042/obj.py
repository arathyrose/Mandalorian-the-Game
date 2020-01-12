'''
base class for any object on the board
'''
import colored_printing


class obj:
    def __init__(self, x, y, h, w, style, ty):
        self.x = x
        self.y = y
        self.h = h
        self.w = w
        self.style = style
        self.type = ty

    def write_self_on_board(self, gameboard):
        for i in range(self.h):
            for j in range(self.w):
                if(self.style[i][j] != ' '):
                    gameboard.board[i+self.x][j+self.y][0] = self.style[i][j]
                    gameboard.board[i+self.x][j+self.y][1] = self.type
                else:
                    gameboard.board[i+self.x][j+self.y][0] = " "
                    gameboard.board[i+self.x][j+self.y][1] = "Normal"

    def destroy_self(self, gameboard):
        for i in range(self.h):
            for j in range(self.w):
                gameboard.board[i+self.x][j+self.y][0] = " "
                gameboard.board[i+self.x][j+self.y][1] = "Normal"

    def print_direct(self):
        print("\033[s")  # save position
        for i in range(self.h):
            for j in range(self.w):
                print("\033["+str(self.x+i+1)+";" +
                      str(self.y-j+2)+"H"+colored_printing.color_text(self.style[i][j], self.type))
        print("\033[u")  # restore position
