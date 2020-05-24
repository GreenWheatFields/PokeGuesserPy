import PokeStats
import sys
import GameSetup

results = {}
round = 0


class mainMode(GameSetup.setup):
    def __init__(self, select, mode, gen_select):
        super().__init__()
        # could most likely be replaced by self, but whatever
        self.event, self.values = self.window.read()
        self.main_mode(select, mode, gen_select)


    def main_mode(self, select, mode, gen_select):
        print("INSIDE")
        total_shown = 0
        tries = 0

        if len(select) == 0:
            self.outOfPoke()

        # select[0] = 1
        poke = PokeStats.Pokemon(select[0], mode)  # select[0]
        select.pop(0)
        poke.message(mode)
        self.updateWindow("OLOLOLOLOLOLL")
        # if mode == "easy" or "medium": poke.showImage(mode)
        guess = input("Guess a Pokemon\n")

        while 3 < 4:

            print("start of loop")
            if guess.lower() == poke.name.lower():
                tries += 1
                self.round += 1
                self.logRound(poke, mode, tries, total_shown, gen_select, self.results, self.round)
                self.winMessageAndNextMove(poke, select, mode, tries, total_shown, gen_select)
            elif "hint" == guess.lower() != poke.name.lower():
                total_shown += 1
                self.hints(total_shown, mode, poke)
                print(total_shown)
                guess = input("Guess a Pokemon\n")
            elif guess.lower() != poke.name.lower():
                print("wrong")
                tries += 1
                guess = input("Guess a Pokemon\n")

    def winMessageAndNextMove(self, poke, select, mode, tries, total_shown, gen_select):
        print("Correct! It took you " + str(tries) + " tries.\n Get another Pokemon: Y\n Quit: N "
                                                     "\nReset Game from the beginning: R")
        response = input()
        if response.lower() == "y":
            self.main_mode(select, mode, gen_select)
        elif response.lower() == "n":
            print("Thank you for playing.")
            sys.exit()
        elif response.lower() == "r":
            # reset game
            pass
        print("outside loop")

    def outOfPoke(self):
        print("Out of pokemon, to select a new generation")
        # GameSetup.runPokeGuesser()
        # reset

    def hints(self, total_shown, mode, poke):
        # easy
        if mode == "easy" and total_shown == 1:
            print(poke.name)
        elif mode == "easy" and total_shown > 1:
            print("It's literally {}".format(poke.name))
        # medium
        if mode == "medium" and total_shown == 1:
            print(poke.getDesc("easy"))
        elif mode == "medium" and total_shown == 2:
            poke.showImage("easy")
        elif mode == "medium" and total_shown == 3:
            print(poke.name)
        elif mode == "medium" and total_shown > 3:
            print("Out of hints")
        # hard
        if mode == "hard" and total_shown == 1:
            print("First Appearance: {}".format(poke.firstGens))
        elif mode == "hard" and total_shown == 2:
            print("First letter: {}".format(poke.name[0]))
        elif mode == "hard" and total_shown == 3:
            poke.showImage("medium")
        elif mode == "hard" and total_shown > 3:
            print("Out of hints")

    def logRound(self, poke, mode, tries, total_shown, gen_select, results, roundNum):
        print("inside log round")

        # add stats to a dictionary
        round = "Round " + str(roundNum)
        print(round)
        results.update({round: {"Pokemon ": poke.name, "mode ": mode, "tries ": tries}})
        print(results)
        return results
