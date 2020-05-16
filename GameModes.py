import PokeStats
import sys

total_shown, one = 0, 1
tries = 0


def easy_mode(select, mode):
    global total_shown, one
    one = 1
    print(select)
    while one < 2:
        guess = input("guess a pokemone\n")
        if guess == "lol":
            one += 1

    print("correct")


def medium_mode(select, mode):
    global total_shown, one, tries
    one = 1
    three = 3

    while one < 2:  # might be unesscesary
        if len(select) == 0:
            outOfPoke()
            break
        poke = PokeStats.Pokemon(select[0], mode)  # select[0]
        select.pop(0)
        poke.pokeStats(mode)
        guess = input("Guess a Pokemon\n")
        while 3 < 4:
            if guess.lower() == poke.name.lower():
                tries += 1
                winMessageAndNextMove(poke, select, mode)
            elif "hint" == guess.lower() != poke.name.lower():
                print(poke.desc)
                total_shown += 1
                guess = input("Guess a Pokemon\n")
            elif guess.lower() != poke.name.lower():
                print("wrong")
                tries += 1
                guess = input("Guess a Pokemon\n")


def hard_mode(select):
    global total_shown, one
    one = 1
    print(select)
    while one < 2:
        guess = input("guess a pokemone\n")
        if guess == "lol":
            one += 1


def winMessageAndNextMove(poke, select, mode):
    modes = {"easy": easy_mode,
             "medium": medium_mode,
             "hard": hard_mode}
    print("Correct! It took you " + str(tries) + " tries.\n Get another Pokemon: Y\n Quit: N "
                                                 "\nReset Game from the beginning: R")
    response = input()
    if response.lower() == "y":
        modes[mode](select, mode)
    elif response.lower() == "n":
        print("Thank you for playing.")
        sys.exit()
    elif response.lower() == "r":
        # reset game
        pass
    print("outside loop")


def outOfPoke():
    print("Out of pokemon, to select a new generation")
    # GameSetup.runPokeGuesser()
    #reset
