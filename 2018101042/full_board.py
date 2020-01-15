"""
Denotes the entire board of the game that is pregenerated
Playable area: 

height: 2, screen_height-3
width: screen_length

So I am planning to keep the game of length total_no_screens * length and once that segment is shown then I would just redo this process
"""
import global_stuff
import numpy as np
from coins import coins
import getch
import random
from beam import beam
from powerUp import powerup
from magnet import magnet


class full_board():
    def __init__(self, rows, columns):

        self.rows = rows-5
        self.columns = columns*global_stuff.total_no_screens

        # the first element stores the ASCII char to be printed
        self.board = np.full((self.rows, self.columns, 2),
                             " "*global_stuff.total_no_screens)
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

    def put_coins_block(self, screen_no):
        h = random.randint(2, 7)
        w = random.randint(10, 30)
        xpos = random.randint(3, self.rows-2)  # man anything is enough
        ypos = random.randint(int((screen_no-1)*global_stuff.screen_length),
                              int(screen_no*global_stuff.screen_length))  # 1st screen
        if(global_stuff.debug2 == 1):
            print(ypos)
            getch.getch()
        for i in range(h):
            for j in range(w):
                c = coins(xpos+i, ypos+j)
                try:
                    c.write_self_on_board(self)
                except:
                    continue

    def randomly_add_coins_everywhere(self):
        '''
        Generate coins randomly on the board based on the following metric
        Screen 1    : 2 blocks (need not be distinct)
        Screen 2 - 9: 4 blocks (need not be distinct)
        '''
        if(global_stuff.debug2 == 1):
            print("Generating coins...")
        # SCREEN 1
        for _ in range(2):
            # only the y position i.e. the horizontal position of the coin set keeps changing so...
            self.put_coins_block(1)
        # SCREEN 2 - 9
        for screen in range(2, 10):  # screen loop
            for _ in range(4):  # count loop
                # only the y position i.e. the horizontal position of the coin set keeps changing so...
                self.put_coins_block(screen)

    def put_beam_block(self, ty, screen_no):
        attempt = 0
        while (attempt <= 100):
            try:
                if(ty == "h"):
                    # place it anywhere, as though no one cares
                    xpos = random.randint(2, self.rows-4)
                elif(ty in ["d1", "d2", "v"]):
                    xpos = random.randint(
                        2, self.rows-int(global_stuff.length_of_beam/2)+2*global_stuff.safe_region-3)
                ypos = random.randint(int((screen_no-1)*global_stuff.screen_length), int(
                    screen_no*global_stuff.screen_length))  # 1st screen
                beami = beam(xpos, ypos, ty)
                ifp = 1
                for I in range(beami.h):
                    for J in range(beami.w):
                        if(self.check_if_permissible(xpos+I, ypos+J) == 0):
                            ifp = 0
                            break
                    if(ifp == 0):
                        break
                if(ifp == 1):
                    if(global_stuff.debug2 == 1):
                        print(xpos, ypos)
                        getch.getch()
                    beami.write_self_on_board(self)
                    return
                else:
                    attempt += 1
            except:
                if(global_stuff.debug2 == 1):
                    print("Error")
                    getch.getch()
                attempt += 1

    def randomly_add_beams(self):
        '''
        Generate all kinds of beams randomly on the board based on the following metric
        Screen 0.5 - 5    : 2 blocks (placing if permissible) per beam type
        '''
        for typ in ["h", "v", "d1", "d2"]:
            if(global_stuff.debug2 == 1):
                print("Generating "+typ+" beams....")
            for i in range(1, 6):
                for _ in range(2):
                    self.put_beam_block(typ, i+0.5)

    def put_powerup(self, ty, screen_no):
        attempt = 0
        while (attempt <= 100):
            try:
                xpos = random.randint(5, self.rows-5)
                ypos = random.randint(int((screen_no-1)*global_stuff.screen_length), int(
                    screen_no*global_stuff.screen_length))
                pu = powerup(xpos, ypos, ty)
                if(self.check_if_permissible(xpos, ypos) != 0):
                    if(global_stuff.debug2 == 1):
                        print(xpos, ypos)
                        getch.getch()
                    pu.write_self_on_board(self)
                    return
                else:
                    attempt += 1
            except:
                if(global_stuff.debug2 == 1):
                    print("Error")
                    getch.getch()
                attempt += 1

    def randomly_add_powerups(self):
        if(global_stuff.debug2 == 1):
            print("Generating extra life powerups...")
        for screen in range(1, 10):
            self.put_powerup("ExtraLife", screen)
        if(global_stuff.debug2 == 1):
            print("Generating Speed Up powerups...")
        for screen in range(1, 6):
            self.put_powerup("SpeedBoost", screen)
        if(global_stuff.debug2 == 1):
            print("Generating Shield powerups...")
        for screen in range(1, 6):
            for _ in range(2):
                self.put_powerup("ShieldPU", screen)
        if(global_stuff.debug2 == 1):
            print("Generating Snake powerups...")
        for screen in range(1, 2):
            self.put_powerup("Snek", screen+0.5)

    def check_if_permissible(self, X, Y):
        ''' 
        returns 0 if it is not permissible
        '''
        for i in range(-1, 2):
            for j in range(-1, 2):
                try:
                    if(self.board[X+i][Y+j][1] != 'Normal' and self.board[X+i][Y+j][1] != 'Bg1' and self.board[X+i][Y+j][1] != 'Bg2'):
                        if(global_stuff.debug == 1):
                            print(self.board[X+i][Y+j][1])
                        return 0
                except:
                    continue
        return 1

    def add_magnet(self):
        if(global_stuff.debug == 1):
            print("Generating magnet...")
        if(global_stuff.powerUpTesting == 1):
            kdd = 0
        else:
            kdd = 3
        while(True):
            xpos = random.randint(3, 4)
            ypos = random.randint(
                (kdd-1)*global_stuff.screen_length, kdd*global_stuff.screen_length)
            m = magnet(xpos, ypos)
            try:
                ok = 1
                for i in range(m.h):
                    for j in range(m.w):
                        if(self.check_if_permissible(xpos+i, ypos+j) == 0):
                            ok = 0
                            if(global_stuff.debug == 1):
                                print("Not ok at ", xpos+i, ypos+j)
                            break
                    if(ok == 0):
                        break
                if(ok == 1):
                    m.write_self_on_board(self)
                    global_stuff.magnet_y_pos_fullboard = ypos
                    if(global_stuff.debug == 1):
                        print(xpos, ypos)
                        getch.getch()
                    return
                else:
                    if(global_stuff.debug == 1):
                        print('occupied', xpos, ypos)
            except Exception as e:
                print('ERROR in', xpos, ypos)
                print(e)
                continue

    def prepare_board(self):
        self.generate_background()
        self.randomly_add_coins_everywhere()
        self.randomly_add_beams()
        self.randomly_add_powerups()
        self.add_magnet()
