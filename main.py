import sys
import os


# noinspection SpellCheckingInspection
class player:
    def __init__(self, name):
        self.name = name
        self.maxhealth = 100
        self.health = self.maxhealth
        self.attack = 10


# noinspection SpellCheckingInspection
def main():
    os.system('clear')
    print('Wanna play a game?\n')
    print('1.) Sure')
    print('2.) Alrady am')
    print('3.) No')
    option = input('-> ')
    if option == "1":
        start()
    elif option == "2":
        pass
    elif option == "3":
        sys.exit()
    else:
        print('Smartass, huh?')
        main()


def start():
    os.system('clear')
    print('So, what do they call you?')
    option = input('-> ')
    global PlayerIG
    PlayerIG = player(option)
    start1()


def start1():
    os.system('clear')
    print('%s? Fitting name for a cannon fodder. Your parents must of been seers. Because they sure knew your place '
          'ahead of time.' % PlayerIG.name)

main()
