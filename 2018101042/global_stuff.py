# DEBUG MODE
debug = 0
powerUpTesting = 0
test_enemy = 0

# THE PLAYER PERSONAL STUFF
username = "Player"
score = 0
coins_collected = 0

# GAME CONSTANTS
screen_length = 120
screen_height = 30
length_of_beam = 10
safe_region = 1
frame_refresh_time = 0.05
total_life = 10
total_bullets = 10
total_no_screens = 10
enemy_comes_after = 5
boss_total_life = 200
move_left_time = 0.4
total_time = int(min(enemy_comes_after*2*screen_length *
                     move_left_time, total_no_screens*screen_length*move_left_time))

# GAME RELATED GLOBAL VARIABLES
game_start_time = 0
shown_until = screen_length
lives_remaining = total_life
bullets_left = 3  # count of deployable bullets
boss_life_remaining = boss_total_life
enemy_come = 0
magnet_y_pos_fullboard = 0
time_left = total_time
ball_gravity_count=0

# POWER UP RELATED VARIABLES
speeded = 0
snek = 0
shielded = 0
shielded_power_up_counter = -1
speeded_power_up_counter = -1
snek_power_up_counter = -1
shield_timer = 100
snake_timer = 50
speed_timer = 100

# ENEMY STYLES

enemy_style_1 = [
    [' ', '|', '\\', '_', '/', '/', '|', ' ', ' ', ' ', '/', '_', '('],
    [' ', '_', '/', '(', 'o', ')', '/', ' ', ' ', '/', '_', '(', ' '],
    ['/', '_', '_', '.', '-', '.', ' ', '\\', '/', '_', '_', '(', ' '],
    [' ', ' ', '_', '_', '/', '_', '_', '/', '_', '_', '_', '(', ' '],
    [' ', '¨', '-', '¨', '-', '¨', '-', '¨', '-', '¨', ' ', ' ', ' ']
]

enemy_style_2 = [
    [' ', '|', '\\', '_', '/', '/', '|', ' ', ' ', ' ', '/', '_', '('],
    [' ', '_', '/', '(', 'o', ')', '/', ' ', ' ', '/', '_', '(', ' '],
    ['/', 'o', '_', '.', '-', '.', ' ', '\\', '/', '_', '_', '(', ' '],
    [' ', ' ', '_', '_', '/', '_', '_', '/', '_', '_', '_', '(', ' '],
    [' ', '¨', '-', '¨', '-', '¨', '-', '¨', '-', '¨', ' ', ' ', ' ']
]

enemy_style_dead = [
    [' ', '|', '\\', '_', '/', '/', '|', ' ', ' ', ' ', '/', '_', '('],
    [' ', '_', '/', 'x', 'x', 'x', '/', ' ', ' ', '/', '_', '(', ' '],
    ['/', 'o', '_', '.', '-', '.', ' ', '\\', '/', '_', '_', '(', ' '],
    [' ', ' ', '_', '_', '/', '_', '_', '/', '_', '_', '_', '(', ' '],
    [' ', '¨', '-', '¨', '-', '¨', '-', '¨', '-', '¨', ' ', ' ', ' ']
]

# STUFF TO BE DONE BEFORE THE START OF THE GAME


def homework():
    # FIX THE SHAPE OF THE DRAGON
    for i in enemy_style_1:
        i = i.reverse()
    for i in enemy_style_2:
        i = i.reverse()
    for i in enemy_style_dead:
        i = i.reverse()


# CHECKING IF DEAD VARIABLES
hit_by_a_magnet = 0
touch_boss = 0
boss_dead = 0


def check_if_dead():
    '''
    Checks if the hero is dead or not:
        How did you die?
        How did the game end?
        Answers all these questions
    '''
    if(hit_by_a_magnet == 1):
        return "Death by Magnet"
    elif (lives_remaining <= 0):
        return "No Lives Remaining"
    elif(time_left <= 0):
        return "Time out"
    elif(touch_boss == 1):
        return "Touched Boss"
    elif(boss_dead == 1):
        return "Boss Dead"
    else:
        return "Alive"
