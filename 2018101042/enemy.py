'''
Denotes the boss enemy Viserion, the flying dragon

He inherits from `PERSON` and has the following attributes:

- ice balls
- lives

and the following functions:

- throw ice balls
- follow along y axis
- die
'''


from person import person
import global_stuff
from powerUp import powerup
from ice_balls import ball
import random


class enemy(person):
    def __init__(self):
        super().__init__(2, global_stuff.screen_length-2,
                         5, 13, global_stuff.enemy_style_1, "Enemy")
        self._state = 0
        self.ball = ball()

    def print_direct(self):
        if(self._state == 0):
            self._style = global_stuff.enemy_style_1
        elif(self._state == 1):
            self._style = global_stuff.enemy_style_2
        elif(self._state == 'DEAD'):
            self._style = global_stuff.enemy_style_dead
        super().print_direct()
        if(self.ball.exist == 1):
            self.ball.print_direct()

    def follow(self, h):
        if(global_stuff.debug == 1):
            print("Following ", h._x, self._x, global_stuff.screen_height-5-3)
        if(h._x > self._x):
            if(self._x <= global_stuff.screen_height-9):
                super().move("down")
        elif(h._x < self._x):
            super().move("up")

    def release_balls(self):
        '''
        release those balls so filled with ice
        '''
        if(self.ball.exist == 0):
            p = random.randint(0, 4)
            # print(p)
            self.ball.deploy(self._x+p, self._y)

    def move_balls(self, board, hero):
        self.ball.move_left(board, hero)

    def check_collision(self, board, h):
        '''
        Makes global variable 1 if it is colliding with the hero
        Decrease the boss health if bullet hits the boss
        '''
        bullet_accounted = 0
        for i in range(self._h):
            if(bullet_accounted == 1):
                break
            for j in range(self._w):
                if(board.board[self._x+i][self._y-j][1] == "Bullet"):
                    global_stuff.boss_life_remaining -= 1
                    bullet_accounted = 1
                    break
        for i in range(self._h):
            for j in range(self._w):
                for k in range(h._h):
                    for l in range(h._w):
                        if((self._x+i, self._y-j) == (h._x+k, h._y-l)):
                            global_stuff.touch_boss = 1
                            return
        # otherwise check if the ball is colliding with anything
        self.ball.check_collision(board, h)
