'''
Denotes the large yellow laser/fire beams

It inherits from OBSTACLES and has the following attributes:

- length
- orientation

and has the following functions

- check if it is colliding with the player
- be destroyed
'''
from obstacle import obstacle

class beam(obstacle):
    def __init__(self,xpos,ypos,orientation):
        if(orientation=="horizontal" or orientation=="h"):
            # beams are of dimensions 2*safe_region+1 x length_of_beam
            length_of_beam=10
            safe_region=1
            k=[]
            l=[' ']*length_of_beam
            for _ in range(safe_region):
                k.append(l)
            l=['█']
            for _ in range(length_of_beam-2):
                l+='-'
            l+='█'
            k.append(l)
            l=[' ']*length_of_beam
            for _ in range(safe_region):
                k.append(l)
            super().__init__(xpos,ypos,2*safe_region+1,length_of_beam,k,"Hbeam")
        
