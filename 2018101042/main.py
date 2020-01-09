import os
from colorama import init, Fore, Back, Style
from termcolor import colored 

def clrscr():
    os.system('tput reset')
if __name__ == "__main__":
    clrscr()
    print()