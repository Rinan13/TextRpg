import sys
import os
import random
import textwrap

# Player #
# noinspection SpellCheckingInspection
class player:
    def __init__(self, name):
        self.name = name
        self.hp = 100
        self.maxhp = self.hp
        self.attack = 10
        self.mp = 50        # Mana
        self.sp = 2         # Spell points, can be comsumed to learn spells
        self.ap = 3         # Action points - consumed to take action in battle. Refills every turn.
        self.player_spells = []     # Spells, learned by the player.
        self.combined_spells = []   # Spells, combined by the player
        self.active_effects = []    # Current status effects, affecting player.


# noinspection SpellCheckingInspection
def main_menu():
    os.system('clear')
    print('Wanna play a game?\n')
    print('1.) Sure')
    print('2.) Alrady am')
    print('3.) How?')
    print('4.) No')
    option = input('-> ')
    if option == "1":
        start()
    elif option == "2":
        pass
    elif option == "3":
        pass
    elif option == "4":
        sys.exit()
    else:
        print('Smartass, huh? Type the damn number')
        main_menu()


def start():
    os.system('clear')
    print('So, what do they call you?\n')
    option = input('-> ')
    global PlayerIG
    PlayerIG = player(option)
    start1()


def start1():
    os.system('clear')
    print('%s? Fitting name for a cannon fodder.\n' % PlayerIG.name)


main_menu()
