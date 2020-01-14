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

    def collision_manager(self, board):
        for i in range(2):
            for j in range(2):
                """ if(board.board[self.x+i][self.y+j][1] == 'Coin'):
                    global_stuff.score += 10  # 10 score per coin collected by hero
                    # 5 score per coin collected by the bullet
                    global_stuff.coins_collected += 1 """
                what_is_destroyed = board.destroy_object(self.x+i, self.y+j)
                if(global_stuff.debug == 1):
                    print(what_is_destroyed)
                if(what_is_destroyed == 'Coin'):
                    global_stuff.coins_collected += 1
                    global_stuff.score += 10
                elif(what_is_destroyed == 'Hbeam' or what_is_destroyed == 'Vbeam' or what_is_destroyed == 'Dbeam1' or what_is_destroyed == 'Dbeam2'):
                    global_stuff.lives_remaining -= 1
                elif(what_is_destroyed == 'ExtraLife'):
                    p = powerup(self.x+i, self.y+j, 'ExtraLife')
                    p.collect(board)
                elif(what_is_destroyed == 'ShieldPU'):
                    p = powerup(self.x+i, self.y+j, 'ShieldPU')
                    p.collect(board)
                elif(what_is_destroyed == 'SpeedBoost'):
                    p = powerup(self.x+i, self.y+j, 'SpeedBoost')
                    p.collect(board)
                elif(what_is_destroyed == 'Snek'):
                    p = powerup(self.x+i, self.y+j, 'Snek')
                    p.collect(board)
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
