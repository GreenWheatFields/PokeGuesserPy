import GameModes
import random
from random import shuffle


def runPokeGuesser():
    gen_selector()
    mode_select(select)


def gen_selector():
    global select
    gen_select = input("Welcome message. Select generation, gen 1 -7 or All\n")
    while 1 < 2:
        if gen_select.lower() == "gen 1":
            upper_bind = 151
            lower_bind = 1
            break
        elif gen_select.lower() == "gen 2":
            upper_bind = 251
            lower_bind = 152
            break
        elif gen_select.lower() == "gen 3":
            upper_bind = 386
            lower_bind = 252
            break
        elif gen_select.lower() == "gen 4":
            upper_bind = 493
            lower_bind = 387
            break
        elif gen_select.lower() == "gen 5":
            upper_bind = 649
            lower_bind = 494
            break
        elif gen_select.lower() == "gen 6":
            upper_bind = 721
            lower_bind = 650
            break
        elif gen_select.lower() == "gen 7":
            upper_bind = 807
            lower_bind = 722
            break
        elif gen_select.lower() == "all":
            upper_bind = 807
            lower_bind = 1
            break
        else:
            gen_select = input("Unrecognized input:\n")

    select = []

    for i in range(lower_bind, upper_bind + 1):
        select.append(i)
        shuffle(select)

    print(gen_select.capitalize() + " Selected: ")

    return select


def mode_select(select):
    while 1 < 2:
        mode = input("Now select a mode, easy medium, hard\n")
        if mode.lower() == "easy":
            GameModes.easy_mode(select)
            break
        elif mode.lower() == "medium":
            GameModes.medium_mode(select)
            # print("placeholder")
            break
        elif mode.lower() == "hard":
            # GameModes.hard_mode(select)
            print("placeholder")
            break
        else:
            print("incorrect")


runPokeGuesser()
