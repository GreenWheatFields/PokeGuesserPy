import PokeStats
import sys
import GameSetup
import PySimpleGUI as sg
import time


class mainMode():
    def __init__(self, select, mode, gen_select):
        # intialize GUI
        self.imLocation = r"res\\16627.png"
        self.imageElem = sg.Image(filename=self.imLocation, key='SHOW', size=(150, 150))
        self.message = "PRESS ENTER TWICE TO LOAD POKEMON\n"
        self.input = sg.InputText(key='-IN-', size=(90, 12), do_not_clear=False)
        self.prompt = sg.Text('Response', size=(20, 1))
        self.introMessage = sg.Text(self.message, size=(45, 30), key='message')

        self.layout = [[self.imageElem, self.introMessage],
                       [self.prompt, sg.Text(size=(15, 1), key='-OUTPUT-')],
                       [self.input],
                       [sg.Button('Show', bind_return_key=True), sg.Button('Exit')],
                       ]
        self.window = sg.Window('PokeGuesser', self.layout)

        self.window.read()

        self.results = {}
        self.round = 0

        self.hasLoadedPokemon = False
        self.newRound = False

        # could most likely be replaced by self, but whatever
        self.main_mode(select, mode, gen_select)

    def main_mode(self, select, mode, gen_select):

        print("INSIDE")
        total_shown = 0
        tries = 0

        if len(select) == 0:
            self.outOfPoke()

        try:
            poke = PokeStats.Pokemon(select[0], mode)
        except IndexError:
            print("index error. try again")
            sys.exit()

        select.pop(0)
        poke.message(mode)

        # if mode == "easy" or "medium": poke.showImage(mode)
        while True:

            self.event, self.values = self.window.read()

            print(self.event, self.values)
            print(poke.name)
            if self.event in (None, 'Exit'):
                self.window.close()
                sys.exit()
            if self.event == 'Show':
                print(self.values)
                if not self.hasLoadedPokemon:
                    self.updateWindow2(poke.message(mode))
                    self.imageElem.Update(data=poke.showImage(mode), size=(300, 300))
                    self.hasLoadedPokemon = True
                elif self.hasLoadedPokemon and not self.newRound:
                    guess = self.values['-IN-']

                    while 3 < 4:

                        print("start of loop")
                        if guess.lower() == poke.name.lower():
                            tries += 1
                            self.round += 1
                            self.logRound(poke, mode, tries, total_shown, gen_select, self.round)
                            print("outside log rounf")
                            self.winMessageAndNextMove(poke, select, mode, tries, total_shown, gen_select)
                            self.newRound = True
                            break
                        elif "hint" == guess.lower() != poke.name.lower():
                            total_shown += 1
                            self.updateWindow2(self.hints(total_shown, mode, poke), append=True)
                            print(total_shown)
                            break
                        elif guess.lower() != poke.name.lower():
                            tries += 1
                            self.prompt.Update("Incorrect. Tries: {}".format(tries))
                            break
                elif self.hasLoadedPokemon and self.newRound:
                    self.winMessageAndNextMove(poke, select, mode, tries, total_shown, gen_select)

    def winMessageAndNextMove(self, poke, select, mode, tries, total_shown, gen_select):
        self.updateWindow2("Correct! It took you " + str(tries) + " tries.\n Get another Pokemon: Y\n Quit: N "
                                                                  "\nReset Game from the beginning: R")
        response = self.values['-IN-']

        if str(response).lower() == "y":
            self.hasLoadedPokemon = self.newRound = False
            self.main_mode(select, mode, gen_select)
        elif response.lower() == "n":
            print("Thank you for playing.")
            sys.exit()
        elif response.lower() == "r":
            # reset game
            GameSetup.setup()


    def outOfPoke(self):
        print("Out of pokemon, to select a new generation")
        # GameSetup.runPokeGuesser()
        # reset

    def hints(self, total_shown, mode, poke):
        # easy
        if mode == "easy" and total_shown == 1:
            return poke.name
        elif mode == "easy" and total_shown > 1:
            return "It's literally {}".format(poke.name)
        # medium
        if mode == "medium" and total_shown == 1:
            return poke.getDesc("easy")
        elif mode == "medium" and total_shown == 2:
            poke.showImage("easy")
        elif mode == "medium" and total_shown == 3:
            return poke.name
        elif mode == "medium" and total_shown > 3:
            return "Out of hints"
        # hard
        if mode == "hard" and total_shown == 1:
            return "First Appearance: {}".format(poke.firstGens)
        elif mode == "hard" and total_shown == 2:
            return "First letter: {}".format(poke.name[0])
        elif mode == "hard" and total_shown == 3:
            poke.showImage("medium")
        elif mode == "hard" and total_shown > 3:
            return "Out of hints"

    def logRound(self, poke, mode, tries, total_shown, gen_select, roundNum):
        print("inside log round")

        # add stats to a dictionary
        round = "Round " + str(roundNum)
        print(round)
        self.results.update({round: {"Pokemon ": poke.name, "mode ": mode, "tries ": tries}})
        print(self.results)

    def updateWindow2(self, message, append=False):
        if not append:
            self.introMessage.Update(message)
        elif append:
            self.introMessage.Update("{}\n{}".format(self.introMessage.Get(), message))


if __name__ == '__main__':
    # for testing
    select = [1, 2, 3, 4, 5 ,6 ,7 ,8 ,9]
    mainMode(select, "easy", "gen 1")
