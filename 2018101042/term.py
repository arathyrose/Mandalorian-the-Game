"""
Has those functions related to the terminal

- clrscr

Clears the terminal screen

- next_play

Repositions the pointer to the top left corner of the screen for the next game
"""

import subprocess as sp


def clrscr():
    '''
    Clears the terminal screen
    '''
    sp.call('clear', shell=True)


def next_play():
    ''' 
    Repositions the pointer to the top left corner of the screen for the next game
    '''
    print("\033[0;0H", end="")
