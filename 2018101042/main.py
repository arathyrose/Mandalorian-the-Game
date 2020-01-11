import os
from colorama import init, Fore, Back, Style
from termcolor import colored
import global_stuff
import inputs
import term
import gameboard
import time
if __name__ == "__main__":
    term.clrscr()

    board=gameboard.gameboard(40,200)
    print("THE MANDALORIAN : THE GAME")
    print()
    print("Enter your name: ")
    global_stuff.username = input()
    # set up input
    keys=inputs.NBInput()
    keys.nbTerm() #enable non-blocking input
    keys.flush()

    global_stuff.game_start_time=time.time() #get the start time of the game

    # the game loop goes here
    while(1):
        term.clrscr()
        # TODO: print the board
        board.print()
        
        # get input
        if keys.kbHit(): # poll for input
            global_stuff.control_pressed = keys.getCh()
            print(global_stuff.control_pressed)
            if(global_stuff.control_pressed=='q'):
                break
        time.sleep(0.2)
    #...
    term.clrscr()
    print("GAME OVER")
    print()
    print("Congratulations "+global_stuff.username)
    print("Score: "+str(global_stuff.score))
    print("Time left: "+str(global_stuff.time_left))
    global_stuff.username = input()
