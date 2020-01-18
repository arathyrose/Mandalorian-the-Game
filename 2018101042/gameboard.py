'''
gameboard
=========

This class denotes the game board that is currently being displayed on the screen.

Data Members:
-------------

- rows

Denotes the number of rows (horizontal things) : 50

- columns

Denotes the number of columns (vertical things) : 200

- board

Denotes the canvas were we would draw everything

Member Functions:
-----------------

- Constructor

Initialises the full board with the length, width and the board matrix
Here, the board matrix is kept as public, to allow all the functions to gain a direct access to it
Each element in the board matrix is of the form (ASCII CHARACTER, TYPE OF THE OBSTACLE/BOARD ELEMENT) at that spot
Also sets up the top bar(the first two rows), bottom bar(the last three rows) and prints all the accessories of the game board

- gamename_display

Displays the game name on the top left corner of the game board on the top bar

- score_update

Displays the score on the top right corner of the game board on the top bar 
The score is left padded with 0s

- coins_collected_update

Displays the number of coins collected by the hero on the top right corner of the bottom bar

- life_display

Displays the life remaining of the hero on the top left corner of the bottom bar
The life remaining is drawn using black blocks like a progress bar

- time_display

Displays the time remaining for the hero to save Baby Yoda on left side of the bottom bar
The time remaining is drawn using black blocks like a progress bar

- game_progress_display

Displays the progress, i.e. how close the hero is to see the boss, on left side of the bottom bar
The progress is drawn using black blocks like a progress bar

- bullets_display

Displays the number of bullets that are ready to be deployed but not deployed yet on the right side of the bottom bar

- display_powerups_active

Displays those powerups that are active on the right side of the bottom bar

- print_enemy_life

Displays the life remaining of the enemy on the top bar when the enemy comes
The life remaining is drawn using black blocks like a progress bar

- prepare_board(self):

Prepares, i.e. updates the board before printing it on the screen

- print(self):

Prints the gameboard onto the screen

- write_full_on_board(self, full_board, start_in):

Writes from the canvas onto the gameboard from the start_in to till the screen is completely filled

- shift_right(self, full_board, line_to_add):

Shift everything to right every .5 seconds

- is_magnet_on_screen(self):

Returns the y coordinate of the magnet if it is on the screen, otherwise return -1

- destroy_object(self, X, Y):  

Destroys whatever object is there at position X,Y completely and returns the object type
This function deals only with coins, beams and powerups
However since magnets cannot be destoyed, if the current position has a magnet, then it does not destroy it

'''

import numpy as np
from colored_printing import color_text
import global_stuff
from full_board import full_board
import time
from powerUp import powerup


class gameboard:
    def __init__(self, rows, columns):
        '''
        Initialises the full board with the length, width and the board matrix
        Here, the board matrix is kept as public, to allow all the functions to gain a direct access to it
        Each element in the board matrix is of the form (ASCII CHARACTER, TYPE OF THE OBSTACLE/BOARD ELEMENT) at that spot
        Also sets up the top bar(the first two rows), bottom bar(the last three rows) and prints all the accessories of the game board
        '''
        self.__rows = rows
        self.__columns = columns
        self.board = np.full((rows, columns, 2), ' '*10)
        # The top bar
        for i in range(0, 2):
            for j in range(self.__columns):
                self.board[i][j][0] = ' '
                self.board[i][j][1] = 'Top Bar'
        # The game body
        for i in range(2, self.__rows-3):
            for j in range(self.__columns):
                self.board[i][j][0] = ' '
                self.board[i][j][1] = 'Normal'
        # the bottom bar
        for i in range(self.__rows-3, self.__rows):
            for j in range(self.__columns):
                self.board[i][j][0] = ' '
                self.board[i][j][1] = 'Bottom Bar'
        self.gamename_display()

    def gamename_display(self):
        '''
        Displays the game name on the top left corner of the game board on the top bar
        '''
        gamename = 'THE MANDALORIAN: THE GAME'
        leng = len(gamename)
        startat = 2
        for i in range(leng):
            self.board[0][i+startat][0] = gamename[i]

    def score_update(self):
        '''
        Displays the score on the top right corner of the game board on the top bar 
        The score is left padded with 0s
        '''
        scorename = 'SCORE: '+str(global_stuff.score).rjust(10, '0')
        leng = len(scorename)
        startat = self.__columns-2-leng
        for i in range(leng):
            self.board[0][i+startat][0] = scorename[i]

    def coins_collected_update(self):
        '''
        Displays the number of coins collected by the hero on the top right corner of the bottom bar
        '''
        scorename = 'COINS COLLECTED:   ' + \
            str(global_stuff.coins_collected).rjust(5, ' ')
        leng = len(scorename)
        startat = int(self.__columns/2)+5
        for i in range(leng):
            self.board[self.__rows-1][i+startat][0] = scorename[i]

    def life_display(self):
        '''
        Displays the life remaining of the hero on the top left corner of the bottom bar
        The life remaining is drawn using black blocks like a progress bar
        '''
        # Print the word life
        lf = 'LIFE:     '
        leng = len(lf)
        for i in range(leng):
            self.board[self.__rows-3][i][0] = lf[i]
        # Print the life bar
        percentage_to_fill = global_stuff.lives_remaining/global_stuff.total_life
        totwid = int(self.__columns/2-10)
        fill = int(percentage_to_fill*totwid)
        k = ''
        for _ in range(fill):
            k += '█'
        for _ in range(fill, totwid):
            k += ' '
        ln = len(k)
        for i in range(ln):
            self.board[self.__rows-3][i+leng][0] = k[i]
            self.board[self.__rows-3][i+leng][1] = 'Life'

    def time_display(self):
        '''
        Displays the time remaining for the hero to save Baby Yoda on left side of the bottom bar
        The time remaining is drawn using black blocks like a progress bar
        '''
        # Print the word 'TIME LEFT'
        lf = 'TIME LEFT:'
        leng = len(lf)
        for i in range(leng):
            self.board[self.__rows-2][i][0] = lf[i]
        # Print the time bar
        global_stuff.time_left = int(
            global_stuff.total_time+global_stuff.game_start_time-time.time())
        percentage_to_fill = global_stuff.time_left/global_stuff.total_time
        totwid = int(self.__columns/2-10)
        fill = int(percentage_to_fill*totwid)
        k = ''
        for _ in range(fill):
            k += '█'
        for _ in range(fill, totwid):
            k += ' '
        ln = len(k)
        for i in range(ln):
            self.board[self.__rows-2][i+leng][0] = k[i]
            self.board[self.__rows-2][i+leng][1] = 'Time'

    def shield_pu_display(self):
        '''
        Displays the shield powerup, that is, if it is active or not and so on
        '''
        # Print the word Shield
        lf='SHIELD:            '
        leng = len(lf)
        for i in range(leng):
            self.board[self.__rows-2][i+int(global_stuff.screen_length/2)+5][0] = lf[i] 
        # Print the progress bar
        if(global_stuff.shield_is_active==0):
            percentage_to_fill=global_stuff.shield_countdown/global_stuff.shield_total_countdown
            typ='ShieldedHero'
        else:
            percentage_to_fill=global_stuff.shield_active_timer/global_stuff.shield_total_active_time
            typ='ShieldPU'
        if(percentage_to_fill >= 1):
            percentage_to_fill = 1
        totwid = int(self.__columns/2-30)
        fill = int(percentage_to_fill*totwid)
        k = ''
        for _ in range(fill):
            k += '█'
        for _ in range(fill, totwid):
            k += ' '
        ln = len(k)
        for i in range(ln):
            self.board[self.__rows-2][i+leng+int(global_stuff.screen_length/2)+5][0] = k[i]  # put the time left
            self.board[self.__rows-2][i+leng+int(global_stuff.screen_length/2)+5][1] = typ

    def game_progress_display(self):
        '''
        Displays the progress, i.e. how close the hero is to see the boss, on left side of the bottom bar
        The progress is drawn using black blocks like a progress bar
        '''
        # Print the word progress
        lf = 'PROGRESS: '
        leng = len(lf)
        for i in range(leng):
            self.board[self.__rows-1][i][0] = lf[i] 
        # Print the progress bar
        progress = global_stuff.shown_until-global_stuff.screen_length
        percentage_to_fill = progress / \
            ((global_stuff.enemy_comes_after-1)*global_stuff.screen_length)
        if(percentage_to_fill >= 1):
            percentage_to_fill = 1
        totwid = int(self.__columns/2-10)
        fill = int(percentage_to_fill*totwid)
        k = ''
        for _ in range(fill):
            k += '█'
        for _ in range(fill, totwid):
            k += ' '
        ln = len(k)
        for i in range(ln):
            self.board[self.__rows-1][i+leng][0] = k[i]  # put the time left
            self.board[self.__rows-1][i+leng][1] = 'Progress'
    def bullets_display(self):
        '''
        Displays the number of bullets that are ready to be deployed but not deployed yet on the right side of the bottom bar
        '''
        lf = 'BULLETS LEFT:      '
        k = ''
        for _ in range(global_stuff.bullets_left):
            k += '> '
        for _ in range(global_stuff.bullets_left, global_stuff.total_bullets):
            k += '  '
        lf += k
        leng = len(lf)
        for i in range(leng):
            self.board[self.__rows-3][i +
                                      int(global_stuff.screen_length/2)+5][0] = lf[i]

    def display_powerups_active(self):
        '''
        Displays those powerups that are active on the right side of the bottom bar
        '''
        l = 'POWERUPS ACTIVE:   '
        leng = len(l)
        i = int(global_stuff.screen_length/2)+5
        for j in range(leng):
            self.board[self.__rows-2][i][0] = l[j]
            i += 1
        if(global_stuff.snek == 1):
            p = powerup(self.__rows-2, i, 'Snek')
            p.write_self_on_board(self)
        else:
            self.board[self.__rows-2][i][0] = ' '
            self.board[self.__rows-2][i][1] = 'Bottom Bar'
        i += 1
        self.board[self.__rows-2][i][0] = ' '
        self.board[self.__rows-2][i][1] = 'Bottom Bar'
        i += 1
        if(global_stuff.shielded == 1):
            p = powerup(self.__rows-2, i, 'ShieldPU')
            p.write_self_on_board(self)
        else:
            self.board[self.__rows-2][i][0] = ' '
            self.board[self.__rows-2][i][1] = 'Bottom Bar'
        i += 1
        self.board[self.__rows-2][i][0] = ' '
        self.board[self.__rows-2][i][1] = 'Bottom Bar'
        i += 1
        if(global_stuff.speeded == 1):
            p = powerup(self.__rows-2, i, 'SpeedBoost')
            p.write_self_on_board(self)
        else:
            self.board[self.__rows-2][i][0] = ' '
            self.board[self.__rows-2][i][1] = 'Bottom Bar'
        i += 1
        self.board[self.__rows-2][i][0] = ' '
        self.board[self.__rows-2][i][1] = 'Bottom Bar'
        i += 1

    def print_enemy_life(self):
        '''
        Displays the life remaining of the enemy on the top bar when the enemy comes
        The life remaining is drawn using black blocks like a progress bar
        '''
        # Print the word enemy
        lf = 'ENEMY: '
        leng = len(lf)
        for i in range(leng):
            self.board[1][i][0] = lf[i] 
        # Print the enemy life bar
        percentage_to_fill = global_stuff.boss_life_remaining / global_stuff.boss_total_life
        if(percentage_to_fill <= 0):
            global_stuff.boss_dead = 1
        totwid = int(self.__columns-10)
        fill = int(percentage_to_fill*totwid)
        k = ''
        for _ in range(fill):
            k += '█'
        for _ in range(fill, totwid):
            k += ' '
        ln = len(k)
        for i in range(ln):
            self.board[1][i+leng][0] = k[i]  
            self.board[1][i+leng][1] = 'Life'
    def prepare_board(self):
        '''
        Prepares, i.e. updates the board before printing it on the screen
        '''
        self.score_update()
        self.life_display()
        self.time_display()
        self.bullets_display()
        self.game_progress_display()
        self.display_powerups_active()
        self.coins_collected_update()
        self.shield_pu_display()
    def print(self):
        '''
        Prints the gameboard onto the screen
        '''
        self.prepare_board()
        if(global_stuff.enemy_come == 1):
            self.print_enemy_life()
        for i in range(self.__rows):
            for j in range(self.__columns):
                print(color_text(self.board[i][j]
                                 [0], self.board[i][j][1]), end='')
            print()

    def write_full_on_board(self, full_board, start_in):
        ''' 
        Writes from the canvas onto the gameboard from the start_in to till the screen is completely filled
        '''
        try:
            for i in range(0, full_board.getrows()):  # all the rows from blahblahblah
                for j in range(0, self.__columns):  # all the columns from teh gameboard
                    self.board[i+2][j] = full_board.board[i][j+start_in]
        except Exception as e:
            print(i, j)
            print(full_board.getrows(), self.__columns)
            print(self.board.shape, full_board.board.shape)
            print(e)

    def shift_right(self, full_board, line_to_add):
        '''
        Shift everything to right every .5 seconds
        '''
        for i in range(full_board.getrows()):
            for j in range(self.__columns-1):
                self.board[i+2][j] = self.board[i+2][j+1]
        for i in range(full_board.getrows()):
            self.board[i+2][self.__columns -
                            1] = full_board.board[i][line_to_add]

    def is_magnet_on_screen(self):
        '''
        Returns the y coordinate of the magnet if it is on the screen, otherwise return -1
        '''
        position = global_stuff.magnet_y_pos_fullboard - \
            global_stuff.shown_until+global_stuff.screen_length
        if(position < global_stuff.screen_length and position >= -7):
            return position
        return 'NOT ON SCREEN'

    def destroy_object(self, X, Y):  
        '''
        Destroys whatever object is there at position X,Y completely and returns the object type
        This function deals only with coins, beams and powerups
        However since magnets cannot be destoyed, if the current position has a magnet, then it does not destroy it
        '''
        # No collision
        if(self.board[X][Y][1] == 'Normal' or self.board[X][Y][1] == 'Bg1' or self.board[X][Y][1] == 'Bg2'):
            return 'No collision'
        # Coin 
        elif(self.board[X][Y][1] == 'Coin'):
            self.board[X][Y][0] = ' '
            self.board[X][Y][1] = 'Normal'
            return 'Coin'
        # Horizontal beam
        elif(self.board[X][Y][1] == 'Hbeam'):  
            try:  # for left side
                i = 0
                while (self.board[X][Y+i][1] == 'Hbeam'):
                    self.board[X][Y+i][0] = ' '
                    self.board[X][Y+i][1] = 'Normal'
                    i += 1
            except:
                pass
            try:  # for right side
                i = 1
                while (self.board[X][Y-i][1] == 'Hbeam'):
                    self.board[X][Y-i][0] = ' '
                    self.board[X][Y-i][1] = 'Normal'
                    i += 1
            except:
                pass
            return 'Hbeam'
        # Vertical beam
        elif (self.board[X][Y][1] == 'Vbeam'): 
            try:  # for up or down
                i = 0
                while (self.board[X+i][Y][1] == 'Vbeam'):
                    self.board[X+i][Y][0] = ' '
                    self.board[X+i][Y][1] = 'Normal'
                    i += 1
            except:
                pass
            try:  # for the other thing
                i = 1
                while (self.board[X-i][Y][1] == 'Vbeam'):
                    self.board[X-i][Y][0] = ' '
                    self.board[X-i][Y][1] = 'Normal'
                    i += 1
            except:
                pass
            return 'Vbeam'
        # Diagonal 1 beam
        elif (self.board[X][Y][1] == 'Dbeam1'): 
            try:  
                i = 0
                while (self.board[X+i][Y+i][1] == 'Dbeam1'):
                    self.board[X+i][Y+i][0] = ' '
                    self.board[X+i][Y+i][1] = 'Normal'
                    i += 1
            except:
                pass
            try:  
                i = 1
                while (self.board[X-i][Y-i][1] == 'Dbeam1'):
                    self.board[X-i][Y-i][0] = ' '
                    self.board[X-i][Y-i][1] = 'Normal'
                    i += 1
            except:
                pass
            return 'Dbeam1'
        # Diagonal 2 beam
        elif(self.board[X][Y][1] == 'Dbeam2'): 
            try: 
                i = 0
                while (self.board[X-i][Y+i][1] == 'Dbeam2'):
                    self.board[X-i][Y+i][0] = ' '
                    self.board[X-i][Y+i][1] = 'Normal'
                    i += 1
            except:
                pass
            try: 
                i = 1
                while (self.board[X+i][Y-i][1] == 'Dbeam2'):
                    self.board[X+i][Y-i][0] = ' '
                    self.board[X+i][Y-i][1] = 'Normal'
                    i += 1
            except:
                pass
            return 'Dbeam2'
        # Power-ups
        elif(self.board[X][Y][1] in ['ExtraLife' , 'ShieldPU' , 'SpeedBoost' , 'Snek','ExtraTime']):
            t = self.board[X][Y][1]
            self.board[X][Y][0] = ' '
            self.board[X][Y][1] = 'Normal'
            return t
        # Magnet
        elif(self.board[X][Y][1] == 'Magnet'):
            return 'Magnet'
