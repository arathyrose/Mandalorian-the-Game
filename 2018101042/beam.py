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
from global_stuff import length_of_beam, safe_region # everything in the safe region would be cleared
import numpy as np
class beam(obstacle):
    def __init__(self,xpos,ypos,orientation):
        if(orientation=="horizontal" or orientation=="h"):
            # beam is of dimensions 2*safe_region+1 x length_of_beam+2*safe_region
            # width of the beam is always 1
            k=np.full((2*safe_region+1,length_of_beam+2*safe_region)," ")
            k[safe_region][safe_region]='█'
            for i in range(safe_region+1,safe_region+length_of_beam-1):
                k[safe_region][i]='-'
            k[safe_region][safe_region+length_of_beam-1]='█'
            sh=k.tolist()
            super().__init__(xpos,ypos,2*safe_region+1,length_of_beam+2*safe_region,sh,"Hbeam")
        elif(orientation=="vertical" or orientation=="v"):
            # beam is of dimension int(length_of_beam/2)+2 x 2*safe_region
            k=np.full((int(length_of_beam/2)+2*safe_region,2*safe_region+1)," ")
            k[safe_region][safe_region]='█'
            for i in range(safe_region+1,safe_region+int(length_of_beam/2)-1):
                k[i][safe_region]='|'
            k[safe_region+int(length_of_beam/2)-1][safe_region]='█'
            sh=k.tolist()
            super().__init__(xpos,ypos,int(length_of_beam/2)+2*safe_region,2*safe_region+1,sh,"Vbeam")
        elif(orientation=="diagonal"):
            pass

        
