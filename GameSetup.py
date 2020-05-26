import sys
from random import shuffle
import PySimpleGUI as sg

import GameModes


class setup():
    def __init__(self):

        # intialize GUI
        self.imLocation = r"res\\16627.png"
        self.imageElem = sg.Image(key='SHOW', size=(300, 300))
        self.message = "Welcome to PokeGuesser!\nPlease select a generation of Pokemon, 1 - 7 or 'All'.\n EX: 'gen 6' , 'all'"
        self.input = sg.InputText(key='-IN-', size=(90, 12), do_not_clear=False)
        self.prompt = sg.Text('Response')
        self.introMessage = sg.Text(self.message, size=(15, 15))

        self.layout = [[self.imageElem, self.introMessage],
                       [self.prompt, sg.Text(size=(15, 1), key='-OUTPUT-')],
                       [self.input],
                       [sg.Button('Show', bind_return_key=True), sg.Button('Exit')],
                       ]
        self.window = sg.Window('PokeGuesser', self.layout)

        self.selectedGen = self.selectedMode = False
        self.sameLoop = True

    def build(self):
        global select, gen_select, mode
        while True:

            self.event, self.values = self.window.read()
            print(self.event, self.values)
            # self.gen_selector()
            if self.event in (None, 'Exit'):
                self.window.close()
                sys.exit()
            if self.event == 'Show':
                if not self.selectedGen:
                    select, gen_select = self.gen_selector(self.values['-IN-'])
                elif self.selectedGen and not self.selectedMode:
                    self.selectedMode, mode = self.mode_select(select, gen_select, self.values['-IN-'])
                elif self.selectedGen and self.selectedMode:
                    self.window.close()
                    x = GameModes.mainMode(select, mode, gen_select)
                else:
                    print("here2")

                # x = r"res\\thumb-1920-574726.png"
                # self.imageElem.Update(filename=x, size=(300, 300))

    def runPokeGuesser(self):
        self.build()
        # redudant

    def gen_selector(self, response):
        # should describe max generations and all
        gen_select = response
        print(response)
        
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
                self.introMessage.Update("Invalid entry")
                self.canContinue = False
                return "None", "None"

        select = []

        for i in range(lower_bind, upper_bind + 1):
            select.append(i)

        shuffle(select)

        self.updateWindow(gen_select.capitalize() + " Selected:\n Now select a mode Easy, Medium, or Hard:\n Easy mode: Detailed picture, over 7 in game attributes\n\nMedium: In game sprite, slightly less in game stats.\n\n Hard: 4 in game stats, no picture\n\n Type: 'easy', ' medium' , or 'hard'")
        # self.introMessage.Update(gen_select.capitalize() + " Selected:\n Now select a Mode. easy, medium, or hard")
        self.canContinue = self.selectedGen = True

        return select, gen_select,  # probably redundant

    def mode_select(self, select, gen_select, input):
        mode = str(input)

        if mode.lower() == "easy" or mode.lower() == "medium" or mode.lower() == "hard":
            self.updateWindow("{} mode selected.\n press Enter".format(mode.capitalize()))
            print(mode.lower())
            return True, str(mode).lower()
        else:
            print("here")
            self.updateWindow("Invalid mode: ")
            return False, mode

    def updateWindow(self, message):
        # i have no idea why this needs to be it's own function but it works
        self.introMessage.Update(message)


# runPokeGuesser()
# a = list(range(1, 807))
# shuffle(a)
# a[0] = 1
# GameModes.main_mode(a, "easy")
if __name__ == "__main__":
    setup().runPokeGuesser()
