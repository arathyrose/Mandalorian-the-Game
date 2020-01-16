import global_stuff
import inputs
import term
import gameboard
import time
from person import person
from hero import hero
from coins import coins
from full_board import full_board
from enemy import enemy
from bullet import bullet


if __name__ == '__main__':

    term.clrscr()  # clear the screen

    # SCREEN 1
    print('THE MANDALORIAN : THE GAME')
    print()
    print('Enter your name: ')
    global_stuff.username = input()

    # SET UP THE INPUE
    keys = inputs.NBInput()
    keys.nbTerm()
    keys.flush()

    # MAKE THE BOARDS, HERO AND THE ENEMY
    fb = full_board(global_stuff.screen_height,
                    global_stuff.screen_length)  # full board
    fb.prepare_board()
    board = gameboard.gameboard(
        global_stuff.screen_height, global_stuff.screen_length)  # Partial board displayed on the screen
    # Write to the partial board on the screen
    board.write_full_on_board(fb, 0)
    h = hero()  # Hero
    e = enemy()  # Enemy

    # MAKE THE ENEMY COME IN THE 1st SCREEN IF IN TESTING MODE
    global_stuff.homework()
    if(global_stuff.test_enemy == 1):
        global_stuff.enemy_come = 1

    # BULLETS
    bullet_list = [bullet() for _ in range(10)]
    for i in range(global_stuff.bullets_left):
        bullet_list[i].make_deployable()
    if(global_stuff.debug == 1):
        print('Game starts at '+str(global_stuff.game_start_time))

    # TIME MANAGEMENT
    global_stuff.game_start_time = time.time()  # get the start time of the game
    last_shift_time = global_stuff.game_start_time

    # INITIALISE THE LOCAL COUNTERS USED
    gravity_ok = 0
    restore_bullet = 0

    # OTHER LOCAL GAME VARIABLES
    isdead = 'Alive'

    # GAME LOOP
    while(1):

        # DISPLAY THE BOARD, HERO, BULLETS AND ENEMY(if applicable)
        term.next_play()
        board.print()
        h.print_direct()
        if(global_stuff.enemy_come == 1):
            e.print_direct()
            e.follow(h)  # make the enemy follow our hero
            e.check_collision(board, h)

        # IF IN DEBUG MODE, DISPLAY THE FOLLOWING
        if(global_stuff.debug == 1):
            #  THE SCREEN COLUMN THAT WILL BE DISPLAYED NEXT
            print(global_stuff.shown_until)
            #  WHETHER THE MAGNET IS ON THE SCREEN
            if(board.is_magnet_on_screen() != 'NOT ON SCREEN'):
                print('YES MAGNET ON SCREEN')

        # POLL FOR THE INPUT EVERY FRAME CYCLE
        if keys.kbHit():

            # GET THE INPUT AND STORE IT IN A VARIABLE
            control_pressed = keys.getCh()
            if(global_stuff.debug == 1):
                print(h.get_coord(), control_pressed)

            # MOVE THE HERO AND CHECK FOR HIS COLLISIONS WITH BOTH THE ENEMY AND THE BOARD OBSTACLES
            h.move(control_pressed)
            h.collision_manager(board)
            if(global_stuff.enemy_come == 1):
                e.follow(h)  # make the enemy follow our hero
                e.check_collision(board, h)

            # SHOOT BULLETS BY THE HERO
            if(control_pressed == ' '):
                for i in range(global_stuff.total_bullets):
                    if(bullet_list[i].deploy(h) == 1):
                        break

            # QUIT THE GAME
            elif(control_pressed == 'q'):
                break

            # RESET IT ALL
            control_pressed = None

        # MOVE THE BOARD BACKWARDS EVERY FEW 100s OF MILLISECONDS
        if(time.time()-last_shift_time >= global_stuff.move_left_time):

            last_shift_time = time.time()

            # SHIFT THE BOARD
            if(global_stuff.debug == 1):
                print('SHIFTING EVERYTHING')
            for i in range(global_stuff.total_bullets):
                bullet_list[i].move_right(board)
            board.shift_right(fb, global_stuff.shown_until)
            global_stuff.shown_until += 1

            # CHECK WHETHER ENEMY SHOULD COME
            if(global_stuff.shown_until >= global_stuff.enemy_comes_after*global_stuff.screen_length):
                global_stuff.enemy_come = 1

            # MANAGE ALL COLLISIONS
            h.collision_manager(board)
            if(global_stuff.enemy_come == 1):
                e.follow(h)  # make the enemy follow our hero
                e.check_collision(board, h)

            # ENEMY DOING STUFF ;p
            if(global_stuff.enemy_come == 1):  # add condition later for checking if there is an enemy hero
                e.release_balls()
                e.move_balls(board, h)
                e.check_collision(board, h)

            # MOVE THE HERO DEPENDING ON THE POSITION OF THE MAGNET
            h.magnet_attraction(board)

            # GRAVITY
            gravity_ok += 1
            if(gravity_ok == 2):  # change this to change gravity strength
                h.move('down')
                gravity_ok = 0
                # check for collisions
                h.collision_manager(board)
                if(global_stuff.enemy_come == 1):
                    e.follow(h)  # make the enemy follow our hero
                    e.check_collision(board, h)

            # RESTORE BULLETS ONCE EVERY 5 SHIFTS
            restore_bullet += 1
            if(restore_bullet == 5):
                for i in range(global_stuff.total_bullets):
                    if(bullet_list[i].check_if_deployable() == 0 and bullet_list[i].check_if_exist() == 0):
                        bullet_list[i].make_deployable()
                        global_stuff.bullets_left += 1
                        break
                if(global_stuff.bullets_left > global_stuff.total_bullets):
                    global_stuff.bullets_left = global_stuff.total_bullets
                restore_bullet = 0

            # POWER-UP RUN OUT CHECK

            # SHIELD POWER-UP
            if(global_stuff.shielded == 1):
                global_stuff.shielded_power_up_counter += 1
                if(global_stuff.shielded_power_up_counter >= global_stuff.shield_timer):
                    global_stuff.shielded_power_up_counter = -1
                    global_stuff.shielded = 0

            # SPEED POWER UP
            if(global_stuff.speeded == 1):
                global_stuff.speeded_power_up_counter += 1
                if(global_stuff.speeded_power_up_counter >= global_stuff.speed_timer):
                    global_stuff.speeded_power_up_counter = -1
                    global_stuff.speeded = 0
                    global_stuff.move_left_time *= 2

            # SNAKE POWERUP
            if(global_stuff.snek == 1):
                global_stuff.snek_power_up_counter += 1
                if(global_stuff.snek_power_up_counter >= global_stuff.snake_timer):
                    global_stuff.snek_power_up_counter = -1
                    global_stuff.snek = 0

        # CHECK IF THE GAME IS OVER
        isdead = global_stuff.check_if_dead()
        if(isdead != '' and isdead != 'Alive'):
            break

        # DEFINE THE FRAME RATE
        time.sleep(global_stuff.frame_refresh_time)

    # THE LAST GAME OVER SCREEN
    term.clrscr()
    print('GAME OVER')
    print()
    print('Congratulations '+global_stuff.username)
    print('Score: '+str(global_stuff.score))
    print('Time left: '+str(global_stuff.time_left))
    if(isdead == '' or isdead == 'Alive'):
        print('Baby Yoda still needs your help.. why you quit my friend?')
    else:
        print('Reason of death: '+isdead)
