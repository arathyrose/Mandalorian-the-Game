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
import time
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
        # Adding beautiful stuff
        global_stuff.game_start_time=time.time()
        self.gamename_display()        # put the game name
        self.score_update()        # put the score
        self.life_display()
        self.time_display()
        self.bullets_display()
    def gamename_display(self):
        # put the game name
        gamename = "THE MANDALORIAN: THE GAME"
        leng = len(gamename)
        startat = 2  # int(columns/2-leng/2)
        for i in range(leng):
            self.board[0][i+startat][0] = gamename[i]  # put the game name
    def score_update(self):
        # put the score
        scorename = "SCORE: "+str(global_stuff.score).rjust(10, "0")
        leng = len(scorename)
        startat = self.columns-2-leng
        for i in range(leng):
            self.board[0][i+startat][0] = scorename[i]
    def life_display(self):
        #put the life
        lf="LIFE:     "
        #totally print columns/2 -10 of which all of them are " " except the first life_remaining/total_life
        percentage_to_fill=global_stuff.lives_remaining/global_stuff.total_life
        totwid=int(self.columns/2-10)
        fill=int(percentage_to_fill*totwid)
        k=""
        for _ in range(fill):
            k+="█"
        for _ in range(fill,totwid):
            k+=" "
        lf+=k
        leng=len(lf)
        for i in range(leng):
            self.board[self.rows-3][i][0] = lf[i]  # put the game name
    def time_display(self):
        #put the time
        lf="TIME LEFT:"
        #totally print columns/2 -10 of which all of them are " " except the first few
        global_stuff.time_left=int(global_stuff.total_time-(-global_stuff.game_start_time+time.time()))
        percentage_to_fill=global_stuff.time_left/global_stuff.total_time
        totwid=int(self.columns/2-10)
        fill=int(percentage_to_fill*totwid)
        #print(global_stuff.game_start_time,global_stuff.time_left,fill,totwid)
        k=""
        for _ in range(fill):
            k+="█"
        for _ in range(fill,totwid):
            k+=" "
        lf+=k
        leng=len(lf)
        for i in range(leng):
            self.board[self.rows-2][i][0] = lf[i]  # put the game name
    def bullets_display(self):
        #put the bullets left
        lf="BULLETS LEFT:      "
        k=""
        for _ in range(global_stuff.bullets_left):
            k+="> "
        for _ in range(global_stuff.bullets_left,global_stuff.total_bullets):
            k+="  "
        lf+=k
        leng=len(lf)
        for i in range(leng):
            self.board[self.rows-1][i][0] = lf[i]  # put the game name
    def print(self):
        self.score_update()
        self.life_display()
        self.time_display()
        self.bullets_display()
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

    def destroy_object(self,X,Y): #deals with coins and beams only
        if(self.board[X][Y][1]=='Normal' or self.board[X][Y][1]=='Bg1' or self.board[X][Y][1]=='Bg2' ):
            return "No collision"
        elif(self.board[X][Y][1]=='Coin'): # coin collision is actually not dealt with here, it was included here for name sake
            # nope, collision of coin by bullets does give points but only 5
            # why? Your bullet did the dirty work
            self.board[X][Y][0]=' '
            self.board[X][Y][1]='Normal'
            # global_stuff.score+=5
            return "Coin"
        elif(self.board[X][Y][1]=='Hbeam'): #aah Horizontal beam
            # no matter who touches the beam, the beam disappears... so
            # but what exactly is the beam?
            # all those continuous points on the same line that have the label 'Hbeam' while they say labels are important..
            # the score system will be discussed later
            # I mean, no score for dying
            # 50 for shooting a beam
            try: # for left side
                i=0
                while (self.board[X][Y+i][1]=='Hbeam'):
                    self.board[X][Y+i][0]=' '
                    self.board[X][Y+i][1]='Normal'
                    i+=1
            except:
                pass
            try: # for right side
                i=1
                while (self.board[X][Y-i][1]=='Hbeam'):
                    self.board[X][Y-i][0]=' '
                    self.board[X][Y-i][1]='Normal'
                    i+=1
            except:
                pass
            return 'Hbeam'
        elif (self.board[X][Y][1]=='Vbeam'): # aah verical beam
            try: # for up or down
                i=0
                while (self.board[X+i][Y][1]=='Vbeam'):
                    self.board[X+i][Y][0]=' '
                    self.board[X+i][Y][1]='Normal'
                    i+=1
            except:
                pass
            try: # for the other thing
                i=1
                while (self.board[X-i][Y][1]=='Vbeam'):
                    self.board[X-i][Y][0]=' '
                    self.board[X-i][Y][1]='Normal'
                    i+=1
            except:
                pass
            return 'Vbeam'
        elif (self.board[X][Y][1]=='Dbeam1'): # aah verical beam
            try: # for up or down
                i=0
                while (self.board[X+i][Y+i][1]=='Dbeam1'):
                    self.board[X+i][Y+i][0]=' '
                    self.board[X+i][Y+i][1]='Normal'
                    i+=1
            except:
                pass
            try: # for the other thing
                i=1
                while (self.board[X-i][Y-i][1]=='Dbeam1'):
                    self.board[X-i][Y-i][0]=' '
                    self.board[X-i][Y-i][1]='Normal'
                    i+=1
            except:
                pass
            return 'Dbeam1'
        elif(self.board[X][Y][1]=='Dbeam2'): # aah verical beam
            try: # for up or down
                i=0
                while (self.board[X-i][Y+i][1]=='Dbeam2'):
                    self.board[X-i][Y+i][0]=' '
                    self.board[X-i][Y+i][1]='Normal'
                    i+=1
            except:
                pass
            try: # for the other thing
                i=1
                while (self.board[X+i][Y-i][1]=='Dbeam2'):
                    self.board[X+i][Y-i][0]=' '
                    self.board[X+i][Y-i][1]='Normal'
                    i+=1
            except:
                pass
            return 'Dbeam2'