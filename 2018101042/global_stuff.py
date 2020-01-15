username = "Player"
score = 0
coins_collected = 0

speed = "normal"
power_up_active = [0, 0]
control_pressed = ""
game_start_time = 0
screen_length = 120
screen_height = 30
gravity = 1
shown_until = screen_length

length_of_beam = 10
safe_region = 1

total_life = 10
lives_remaining = total_life
frame_refresh_time = 0.05



bullets_left = 3  # count of deployable bullets
total_bullets = 10


debug = 0
powerUpTesting = 0

total_no_screens = 10
enemy_comes_after = 5
hit_by_a_magnet = 0

speeded = 0
snek = 0
shielded = 0

shielded_power_up_counter = -1
speeded_power_up_counter = -1
snek_power_up_counter = -1

shield_timer = 100
snake_timer = 50
speed_timer = 100

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


def homework():
    for i in enemy_style_1:
        i = i.reverse()
    for i in enemy_style_2:
        i = i.reverse()
    for i in enemy_style_dead:
        i = i.reverse()


touch_boss = 0
boss_total_life = 200
boss_life_remaining = boss_total_life
test_enemy = 0
enemy_come = 0

magnet_y_pos_fullboard = 0

debug1=0
move_left_time = 0.4

if(debug1==1):
    move_left_time = 0.1


total_time = int( enemy_comes_after*2*screen_length * move_left_time)
time_left = total_time

debug2=0
boss_dead=0