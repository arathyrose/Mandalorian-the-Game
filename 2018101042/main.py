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
from coins import coins
from full_board import full_board
from getch  import getch
def put_coins(board):
    for i in range(30):
        c=coins(i,50)
        c.write_self_on_board(board)
if __name__ == "__main__":
    term.clrscr()
    board = gameboard.gameboard(
        global_stuff.screen_height, global_stuff.screen_length)
    h = hero()

    print("THE MANDALORIAN : THE GAME")
    print()
    print("Enter your name: ")
    global_stuff.username = input()
    # set up input
    keys = inputs.NBInput()
    keys.nbTerm()  # enable non-blocking input
    keys.flush()
    
    fb=full_board(global_stuff.screen_height, global_stuff.screen_length)
    fb.generate_background()
    fb.randomly_add_coins_everywhere()

    board.write_full_on_board(fb,0)
    """ print("BOARD")
    #print(board.board)
    for i in range(board.rows):
        for j in range(board.columns):
            print(board.board[i][j][0],board.board[i][j][1])
    
    print("FULL BOARD")
    for i in range(fb.rows):
        for j in range(fb.columns):
            print(fb.board[i][j][0],fb.board[i][j][1])
     """

    global_stuff.game_start_time = time.time()  # get the start time of the game
    print("Game starts at "+str(global_stuff.game_start_time))
    getch()
    last_shift_time=global_stuff.game_start_time
    # the game loop goes here
    while(1):
        term.next_play()
        # TODO: print the board
        # h.write_self_on_board(board)
        board.print()
        h.print_direct()
        #put_coins(board)
        # get input
        if keys.kbHit():  # poll for input
            global_stuff.control_pressed = keys.getCh()
            #h.move("up")
            #print(board.board)
            print(h.x,h.y,global_stuff.control_pressed)
            h.move(global_stuff.control_pressed)
            if(global_stuff.control_pressed == 'q'):
                break
        # TODO: MOVE THE BOARD TO LEFT DEPENDING ON THE TIME
        if(time.time()-last_shift_time>=0.5):
            last_shift_time=time.time()
            print('SHIFTING EVERYTHING')
            board.shift_right(fb,global_stuff.shown_until)
            global_stuff.shown_until+=1
        time.sleep(0.05)
    # ...
    term.clrscr()
    print("GAME OVER")
    print()
    print("Congratulations "+global_stuff.username)
    print("Score: "+str(global_stuff.score))
    print("Time left: "+str(global_stuff.time_left))
    global_stuff.username = input()
