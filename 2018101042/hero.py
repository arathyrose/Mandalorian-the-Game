""" 
Denotes the Mandalorian who is controlled by the player.

He inherits from `PERSON` and has the following attributes:

- bullets

and the following functions:

- move left
- move right
- move up
- move down
- gravity
- Shoot bullets
- be attracted by the magnet 
"""

from person import person
import global_stuff
from powerUp import powerup


class hero(person):
    def __init__(self):
        super().__init__(global_stuff.screen_height - 5,
                         0, 2, 2, [['▄', '['], ['|', '|']], "Hero")
        self.movingUpSpeed = 0
        self.movingDownSpeed = global_stuff.gravity
        self.movingLeftSpeed = 0
        self.movingRightSpeed = 0

    def print_direct(self):
        if(global_stuff.shielded == 1):
            self.type = "ShieldedHero"
            super().print_direct()
        elif(global_stuff.speeded == 1):
            self.type = "SpeededHero"
            super().print_direct()
        else:
            self.type = "Hero"
            super().print_direct()

    def collision_manager(self, board):
        for i in range(2):
            for j in range(2):
                what_is_destroyed = board.destroy_object(self.x+i, self.y+j)
                if(global_stuff.debug == 1):
                #if(1):
                    if(what_is_destroyed!="No collision"):
                        print(what_is_destroyed)
                if(what_is_destroyed == 'Coin'):
                    global_stuff.coins_collected += 1
                    global_stuff.score += 10
                elif(what_is_destroyed == 'Hbeam' or what_is_destroyed == 'Vbeam' or what_is_destroyed == 'Dbeam1' or what_is_destroyed == 'Dbeam2'):
                    if(global_stuff.shielded==1):
                        global_stuff.shielded=0
                    else:
                        global_stuff.lives_remaining -= 1
                elif(what_is_destroyed == 'ExtraLife' or what_is_destroyed == 'ShieldPU' or what_is_destroyed == 'SpeedBoost' or what_is_destroyed == 'Snek'):
                    #print(what_is_destroyed)
                    p = powerup(self.x+i, self.y+j, what_is_destroyed)
                    p.collect(board)
                
                elif(what_is_destroyed == 'Magnet'):
                    global_stuff.hit_by_a_magnet = 1
                    # DIE!
                    # DIE

    def check_if_dead(self):
        """ How did you die?
        How did the game end?
        Answers all these questions
        """
        if(global_stuff.hit_by_a_magnet == 1):
            return "Death by Magnet"
        elif (global_stuff.lives_remaining <= 0):
            return "No Lives Remaining"
        elif(global_stuff.time_left <= 0):
            return "Baby Yoda is already dead, you slow poke!"
        else:
            return "Alive"

    """ def move(self, direction):
        if(direction == 'w'):
            self.movingUpSpeed += 1
            print('up')
        elif(direction == 's'):
            self.movingDownSpeed += 1
            print('down')
        elif(direction == 'd'):
            self.movingRightSpeed += 1
            print('left')
        elif (direction == 'a'):
            self.movingLeftSpeed += 1
            print('right') """


"""   def print_direct(self):
        print("\033[s")  # save position
        for i in range(self.h):
            for j in range(self.w):
                print("\033["+str(self.x+i+1)+";" +
                      str(self.y-j+2)+"H"+self.style[i][j])
        print("\033[u")  # restore position
 """
