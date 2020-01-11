import os
from colorama import init, Fore, Back, Style
from termcolor import colored
import global_stuff
import inputs
import term
import gameboard
import time
from person import person 
from hero import hero
if __name__ == "__main__":
    term.clrscr()
    board=gameboard.gameboard(global_stuff.screen_height,global_stuff.screen_length)
    h=hero()

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
        term.next_play()
        # TODO: print the board
        #h.write_self_on_board(board)
        board.print()
        h.print_direct()
        
        # get input
        if keys.kbHit(): # poll for input
            global_stuff.control_pressed = keys.getCh()
            #print(global_stuff.control_pressed)
            h.move(global_stuff.control_pressed)
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
