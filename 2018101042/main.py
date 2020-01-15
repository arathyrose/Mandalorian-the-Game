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
# from getch  import getch
from enemy import enemy
from bullet import bullet


def put_coins(board):
    for i in range(30):
        c = coins(i, 50)
        c.write_self_on_board(board)


if __name__ == "__main__":
    term.clrscr()
    board = gameboard.gameboard(
        global_stuff.screen_height, global_stuff.screen_length)
    h = hero()
    global_stuff.game_start_time = time.time()  # get the start time of the game

    print("THE MANDALORIAN : THE GAME")
    print()
    print("Enter your name: ")
    global_stuff.username = input()
    # set up input
    keys = inputs.NBInput()
    keys.nbTerm()  # enable non-blocking input
    keys.flush()

    fb = full_board(global_stuff.screen_height, global_stuff.screen_length)
    fb.prepare_board()
    board.write_full_on_board(fb, 0)
    e = enemy()
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
    gravity_ok = 0
    restore_bullet = 0
    bullet_list = [bullet() for _ in range(10)]
    for i in range(global_stuff.bullets_left):
        bullet_list[i].deployable = 1
    if(global_stuff.debug == 1):
        print("Game starts at "+str(global_stuff.game_start_time))
    # getch()
    last_shift_time = global_stuff.game_start_time
    isdead = "Alive"
    global_stuff.homework()
    if(global_stuff.test_enemy == 1):
        global_stuff.enemy_come = 1
    # the game loop goes here
    while(1):
        term.next_play()
        # TODO: print the board
        # h.write_self_on_board(board)
        board.print()
        h.print_direct()
        if(global_stuff.enemy_come == 1):
            e.print_direct()
            e.follow(h)
        if(global_stuff.debug == 1):
            print(global_stuff.shown_until)
        if(global_stuff.enemy_come == 1):
            e.check_collision(board, h)
        # put_coins(board)
        if(global_stuff.debug1==1):
            if(board.is_magnet_on_screen()!="NOT ON SCREEN"):
                print("YES MAGNET ON SCREEN")
        # get input
        if keys.kbHit():  # poll for input
            global_stuff.control_pressed = keys.getCh()
            # h.move("up")
            # print(board.board)
            if(global_stuff.debug == 1):
                print(h.x, h.y, global_stuff.control_pressed)
            h.move(global_stuff.control_pressed)

            h.collision_manager(board)
            if(global_stuff.control_pressed == ' '):
                for i in range(global_stuff.total_bullets):
                    if(bullet_list[i].deploy(h) == 1):
                        break
            elif(global_stuff.control_pressed == 'q'):
                break
            global_stuff.control_pressed = None
        # TODO: MOVE THE BOARD TO LEFT DEPENDING ON THE TIME
        if(time.time()-last_shift_time >= global_stuff.move_left_time):
            last_shift_time = time.time()
            #check if it is time for the enemy to come
            if(global_stuff.shown_until>=global_stuff.enemy_comes_after*global_stuff.screen_length):
                global_stuff.enemy_come=1
            # manage collisions
            h.collision_manager(board)
            # magnet
            is_magnet_on_screen=board.is_magnet_on_screen()
            if(is_magnet_on_screen!="NOT ON SCREEN"):
                if(global_stuff.debug1==1):
                    print("Moving the guy close to ",is_magnet_on_screen)
                if(is_magnet_on_screen+4-1>h.y):
                    h.move("right")
                elif(is_magnet_on_screen+4-1<h.y):
                    h.move("left")
                h.collision_manager(board)
            # left shify everything
            if(global_stuff.debug==1):
                print('SHIFTING EVERYTHING')
            for i in range(global_stuff.total_bullets):
                bullet_list[i].move_right(board)
            board.shift_right(fb, global_stuff.shown_until)
            global_stuff.shown_until += 1
            # Gravity
            gravity_ok += 1
            if(gravity_ok == 2):  # change this to change gravy
                h.move("down")  # gravity :)
                gravity_ok = 0
                h.collision_manager(board)
            # restoring bullets
            restore_bullet += 1
            if(restore_bullet == 5):
                for i in range(global_stuff.total_bullets):
                    if(bullet_list[i].deployable == 0 and bullet_list[i].exist == 0):
                        bullet_list[i].deployable = 1
                        global_stuff.bullets_left += 1
                        break
                if(global_stuff.bullets_left > global_stuff.total_bullets):
                    global_stuff.bullets_left = global_stuff.total_bullets
                restore_bullet = 0
            # powerups ran out ?
            # Shield Hero
            if(global_stuff.shielded == 1):
                global_stuff.shielded_power_up_counter += 1
                if(global_stuff.shielded_power_up_counter >= global_stuff.shield_timer):
                    global_stuff.shielded_power_up_counter = -1
                    global_stuff.shielded = 0
            # speed hero
            if(global_stuff.speeded == 1):
                global_stuff.speeded_power_up_counter += 1
                if(global_stuff.speeded_power_up_counter >= global_stuff.speed_timer):
                    global_stuff.speeded_power_up_counter = -1
                    global_stuff.speeded = 0
                    global_stuff.move_left_time *= 2
            # Snake hero
            if(global_stuff.snek == 1):
                global_stuff.snek_power_up_counter += 1
                if(global_stuff.snek_power_up_counter >= global_stuff.snake_timer):
                    global_stuff.snek_power_up_counter = -1
                    global_stuff.snek = 0
            # Enemy hero
            if(global_stuff.enemy_come == 1):  # add condition later for checking if there is an enemy hero
                e.release_balls()
                e.move_balls(board, h)
        # is hero dead?
        isdead = h.check_if_dead()
        if(isdead != "" and isdead != "Alive"):
            break
        time.sleep(global_stuff.frame_refresh_time)
    # ...
    term.clrscr()
    print("GAME OVER")
    print()
    print("Congratulations "+global_stuff.username)
    print("Score: "+str(global_stuff.score))
    print("Time left: "+str(global_stuff.time_left))
    if(isdead == "" or isdead == "Alive"):
        print("Baby Yoda still needs your help.. why you quit my friend?")
    else:
        print("Reason of death: "+isdead)
    global_stuff.username = input()
