from person import person
from hero import hero
class snake(hero):
    '''
    denotes the snake mode of the hero
    '''
    def __init__(self,x,y):
        super().__init__()
        self._x=x
        self._y=y
        self._h=4
        self._w=4
        self.style=0
        