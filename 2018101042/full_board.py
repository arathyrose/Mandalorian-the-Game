"""
Denotes the entire board of the game that is pregenerated
Playable area: 

height: 2, screen_height-3
width: screen_length

So I am planning to keep the game of length 10 * length and once that segment is shown then I would just redo this process
"""
from global_stuff import screen_length
import numpy as np
from coins import coins
import getch
import random
from beam import beam


class full_board():
    def __init__(self, rows, columns):

        self.rows = rows-5
        self.columns = columns*10

        # the first element stores the ASCII char to be printed
        self.board = np.full((self.rows, self.columns, 2), " "*10)
        # the second element stores the type of the element

    def generate_background(self):
        '''
        generates a background of modern art
        Lol
        '''
        for i in range(self.rows):
            for j in range(self.columns):
                self.board[i][j][0] = " "
                prob = random.random()
                if(prob > 0.9):
                    self.board[i][j][1] = "Bg2"
                else:
                    self.board[i][j][1] = "Bg1"

    def add_coins(self, coins):
        coins.write_self_on_board(self)

    def randomly_add_coins_everywhere(self):  # recheck
        for i in range(11):  # four blocks of coins of random width and height at a distance of at least screen_length/4 apart
            h = random.randint(1, 7)
            w = random.randint(1, 30)+1
            xpos = int(self.rows/2 - 3+random.randint(0, 4-1))
            ypos = int(random.randint(
                0, int(self.columns/11-1)) + (self.columns/11)*i)
            print(ypos)
            getch.getch()
            for i in range(h):
                for j in range(w):
                    c = coins(xpos+i, ypos+j)
                    try:
                        self.add_coins(c)
                    except:
                        continue

    def randomly_add_hbeams(self):
        print("Generating horizontal beams....")
        for i in range(5):
            xpos = int(self.rows/2 - 3+random.randint(0, 4-1)+3)-3
            ypos = int(random.randint(
                3, int(self.columns/5-1)) + (self.columns/5)*i)-3
            print(xpos, ypos, end="hoe\n")
            getch.getch()
            hb = beam(xpos, ypos, "h")
            try:
                hb.write_self_on_board(self)
            except Exception as e:
                print('ERROR in', xpos, ypos)
                print(e)
                continue

    def randomly_add_vbeams(self):
        print("Generating vertical beams....")
        for i in range(5):
            xpos = int(self.rows/2 - 3+random.randint(0, 4-1)+3)-3
            ypos = int(random.randint(
                3, int(self.columns/5-1)) + (self.columns/5)*i)-3
            print(xpos, ypos, end="vert\n")
            getch.getch()
            hb = beam(xpos, ypos, "v")
            try:
                hb.write_self_on_board(self)
            except Exception as e:
                print('ERROR in', xpos, ypos)
                print(e)
                continue

    def randomly_add_coins_dbeams(self):
        print("Generating diagonal beams....")
        for i in range(5):
            xpos = int(self.rows/2 - 3+random.randint(0, 4-1)+3)-3
            ypos = int(random.randint(
                3, int(self.columns/5-1)) + (self.columns/5)*i)-3
            print(xpos, ypos, end="diag\n")
            getch.getch()
            hb = beam(xpos, ypos, "d"+str(random.randint(1, 2)))
            try:
                hb.write_self_on_board(self)
            except Exception as e:
                print('ERROR in', xpos, ypos)
                print(e)
                continue
