import os
from colorama import init, Fore, Back, Style
from termcolor import colored
import global_stuff


def clrscr():
    os.system('tput reset')


if __name__ == "__main__":
    clrscr()
    print("THE MANDALORIAN : THE GAME")
    print()
    print("Enter your name: ")
    global_stuff.username = input()
    # the game loop goes here
    clrscr()
    print("GAME OVER")
    print()
    print("Congratulations "+global_stuff.username)
    print("Score: "+str(global_stuff.score))
    print("Time left: "+str(global_stuff.time_left))
    global_stuff.username = input()
