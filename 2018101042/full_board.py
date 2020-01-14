"""
Denotes the entire board of the game that is pregenerated
Playable area: 

height: 2, screen_height-3
width: screen_length

So I am planning to keep the game of length 10 * length and once that segment is shown then I would just redo this process
"""
import global_stuff
import numpy as np
from coins import coins
import getch
import random
from beam import beam
from powerUp import powerup


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
        if(global_stuff.debug == 1):
            print("Generating coins...")
        for i in range(11):  # four blocks of coins of random width and height at a distance of at least screen_length/4 apart
            h = random.randint(1, 7)
            w = random.randint(1, 30)+1
            xpos = int(self.rows/2 - 3+random.randint(0, 4-1))
            ypos = int(random.randint(
                0, int(self.columns/11-1)) + (self.columns/11)*i)
            if(global_stuff.debug == 1):
                print(xpos, ypos)
                getch.getch()
            for i in range(h):
                for j in range(w):
                    c = coins(xpos+i, ypos+j)
                    try:
                        self.add_coins(c)
                    except:
                        continue

    def randomly_add_hbeams(self):  # randomly adds beams everywhere on the board
        if(global_stuff.debug == 1):
            print("Generating horizontal beams....")
        for i in range(5):
            xpos = int(self.rows/2 - 3+random.randint(0, 4-1)+3)-3
            ypos = int(random.randint(
                3, int(self.columns/5-1)) + (self.columns/5)*i)-3
            if(global_stuff.debug == 1):
                print(xpos, ypos)
                getch.getch()
            hb = beam(xpos, ypos, "h")
            try:
                hb.write_self_on_board(self)
            except Exception as e:
                print('ERROR in', xpos, ypos)
                print(e)
                continue

    def randomly_add_vbeams(self):
        if(global_stuff.debug == 1):
            print("Generating vertical beams....")
        for i in range(5):
            xpos = int(self.rows/2 - 3+random.randint(0, 4-1)+3)-3
            ypos = int(random.randint(
                3, int(self.columns/5-1)) + (self.columns/5)*i)-3
            if(global_stuff.debug == 1):
                print(xpos, ypos)
                getch.getch()
            hb = beam(xpos, ypos, "v")
            try:
                hb.write_self_on_board(self)
            except Exception as e:
                print('ERROR in', xpos, ypos)
                print(e)
                continue

    def randomly_add_dbeams(self):
        if(global_stuff.debug == 1):
            print("Generating diagonal beams....")
        for i in range(5):
            xpos = int(self.rows/2 - 3+random.randint(0, 4-1)+3)-3
            ypos = int(random.randint(
                3, int(self.columns/5-1)) + (self.columns/5)*i)-3
            if(global_stuff.debug == 1):
                print(xpos, ypos)
                getch.getch()
            hb = beam(xpos, ypos, "d"+str(random.randint(1, 2)))
            try:
                hb.write_self_on_board(self)
            except Exception as e:
                print('ERROR in', xpos, ypos)
                print(e)
                continue

    def randomly_add_powerups(self):
        if(global_stuff.debug == 1):
            print("Generating powerups....")
        if(global_stuff.debug == 1):
            print("Generating speed up powerups...")
        # testing remove
        if(global_stuff.powerUpTesting == 1):
            xpos = random.randint(5, self.rows-5)  # height wala cheeze
            ypos = random.randint(10, 14)  # 2,3 , 4,5 and 6,7
            sp = powerup(xpos, ypos, 'sp')
            sp.write_self_on_board(self)

        for i in range(3):
            xpos = random.randint(5, self.rows-5)  # height wala cheeze
            ypos = random.randint((2+2*i)*int(self.columns/10),
                                  (3+2*i)*int(self.columns/10))  # 2,3 , 4,5 and 6,7
            if(global_stuff.debug == 1):
                print(xpos, ypos)
                getch.getch()
            sp = powerup(xpos, ypos, 'sp')
            try:
                if(self.is_location_alright(xpos, ypos) == 1):
                    sp.write_self_on_board(self)
                else:
                    i -= 1
            except Exception as e:
                print('ERROR in', xpos, ypos)
                print(e)
                i -= 1
        if(global_stuff.debug == 1):
            print("Generating Shield Powerups....")
        # testing remove
        if(global_stuff.powerUpTesting == 1):
            xpos = random.randint(5, self.rows-5)  # height wala cheeze
            ypos = random.randint(14, 18)  # 2,3 , 4,5 and 6,7
            sp = powerup(xpos, ypos, 'sh')
            sp.write_self_on_board(self)

        for i in range(3):
            xpos = random.randint(5, self.rows-5)  # height wala cheeze
            # 4,5 and 6,7 and 8,9
            ypos = random.randint(
                (3+2*i)*int(self.columns/10), (4+2*i)*int(self.columns/10))
            if(global_stuff.debug == 1):
                print(xpos, ypos)
                getch.getch()
            sp = powerup(xpos, ypos, 'sh')
            try:
                if(self.is_location_alright(xpos, ypos) == 1):
                    sp.write_self_on_board(self)
                else:
                    i -= 1
            except Exception as e:
                print('ERROR in', xpos, ypos)
                print(e)
                i -= 1
        if(global_stuff.debug == 1):
            print("Generating extra lives....")
        # testing remove
        # testing remove
        if(global_stuff.powerUpTesting == 1):
            xpos = random.randint(5, self.rows-5)  # height wala cheeze
            ypos = random.randint(24, 40)  # 2,3 , 4,5 and 6,7
            sp = powerup(xpos, ypos, 'xl')
            sp.write_self_on_board(self)

        for i in range(10):
            xpos = random.randint(5, self.rows-5)  # height wala cheeze
            # 2,3 , 4,5 and 6,7
            ypos = random.randint(i*int(self.columns/10),
                                  (1+i)*int(self.columns/10))
            if(global_stuff.debug == 1):
                print(xpos, ypos)
                getch.getch()
            sp = powerup(xpos, ypos, 'xl')
            try:
                if(self.is_location_alright(xpos, ypos) == 1):
                    sp.write_self_on_board(self)
                else:
                    i -= 1
            except Exception as e:
                print('ERROR in', xpos, ypos)
                print(e)
                i -= 1
        if(global_stuff.debug == 1):
            print("Generating snake powerup...")

        # testing remove
        if(global_stuff.powerUpTesting == 1):
            xpos = random.randint(5, self.rows-5)  # height wala cheeze
            ypos = random.randint(60, 80)
            sp = powerup(xpos, ypos, 'snek')
            sp.write_self_on_board(self)

        while True:
            xpos = random.randint(5, self.rows-5)  # height wala cheeze
            ypos = random.randint(5*int(self.columns/10),
                                  6*int(self.columns/10))  # 2,3 , 4,5 and 6,7
            if(global_stuff.debug == 1):
                print(xpos, ypos, end="snek\n")
                getch.getch()
            sp = powerup(xpos, ypos, 'snek')
            try:
                if 1:
                    # if(self.is_location_alright(xpos,ypos)==1):
                    sp.write_self_on_board(self)
                    break
            except Exception as e:
                print('ERROR in', xpos, ypos)
                print(e)
                continue

    def is_location_alright(self, X, Y):
        for i in range(-1, 2):
            for j in range(-1, 2):
                try:
                    if(self.board[X+i][Y+j][1] != 'Normal'):
                        return 0
                except:
                    continue
        return 1

    def prepare_board(self):
        self.generate_background()
        self.randomly_add_coins_everywhere()
        self.randomly_add_hbeams()
        self.randomly_add_vbeams()
        self.randomly_add_dbeams()
        self.randomly_add_powerups()
