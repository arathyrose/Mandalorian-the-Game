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

def fire():
    pass
class enemy(person):
    def __init__(self):
        super().__init__(2,global_stuff.screen_length-2, 5, 13, global_stuff.enemy_style_1, "Enemy")
        self.state=0

    def print_direct(self):
        if(self.state==0):
            self.style=global_stuff.enemy_style_1
        elif(self.state==1):
            self.style=global_stuff.enemy_style_2
            fire()
        elif(self.state=='DEAD'):
            self.style=global_stuff.enemy_style_dead
        super().print_direct()
    
    def follow(self,h):
        if(global_stuff.debug==1):
            print("Following ",h.x,self.x,global_stuff.screen_height-5-3)
        if(h.x>self.x):
            if(self.x<=global_stuff.screen_height-9):
                super().move("down")
        elif(h.x<self.x):
            super().move("up")

    def is_colliding(self,h):
        '''
        Makes global variable 1 if it is colliding with the hero
        '''
        for i in range(self.h):
            for j in range(self.w):
                for k in range(h.h):
                    for l in range(h.w):
                        if((self.x+i,self.y-j)==(h.x+k,h.y-l)):
                            global_stuff.touch_boss=1
    