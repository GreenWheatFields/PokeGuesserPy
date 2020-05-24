import GameModes
import GUI
import sys
from random import shuffle
import PySimpleGUI as sg




class setup():
    def __init__(self):
        # intialize GUI
        self.imLocation = r"res\\16627.png"
        self.imageElem = sg.Image(filename=self.imLocation, key='SHOW', size=(300, 300))
        self.message = "Welcome message. Select generation, gen 1 -7 or All\n"
        self.input = sg.InputText(key='-IN-', size=(90, 12), do_not_clear=False)
        self.prompt = sg.Text('Response')
        self.introMessage = sg.Text(self.message, size=(15, 15))

        self.layout = [[self.imageElem, self.introMessage],
                       [self.prompt, sg.Text(size=(15, 1), key='-OUTPUT-')],
                       [self.input],
                       [sg.Button('Show', bind_return_key=True), sg.Button('Exit')],
                       ]
        self.window = sg.Window('PokeGuesser', self.layout)

        gen_select = None
        self.runPokeGuesser()

    def build(self):
        while True:

            self.event, self.values = self.window.read()
            print(self.event, self.values)
            # self.gen_selector()
            if self.event in (None, 'Exit'):
                self.window.close()
                sys.exit()
            if self.event == 'Show':
                # Update the "output" text element to be the value of "input" element
                if self.gen_selector() == False:
                    self.gen_selector()

                # self.input.update("")
                # self.window['-OUTPUT-'].update(values["-IN-"])
                # x = r"res\\thumb-1920-574726.png"
                # self.imageElem.Update(filename=x, size=(300, 300))
                print(self.event)

    def runPokeGuesser(self):
        self.build()
        self.gen_selector()
        self.mode_select(select, gen_select)

    def gen_selector(self):
        global select, gen_select  # might be unesseasry
        gen_select = self.values['-IN-']
        print(gen_select)
        #gen_select = input("Welcome message. Select generation, gen 1 -7 or All\n")
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
                self.introMessage.Update("Incorrect entry detected")
                return False

        select = []

        for i in range(lower_bind, upper_bind + 1):
            select.append(i)

        shuffle(select)

        print(gen_select.capitalize() + " Selected: ")

        return select, gen_select,

    def mode_select(self, select, gen_select):
        while 1 < 2:
            mode = input("Now select a mode, easy medium, hard\n")
            if mode.lower() == "easy":
                GameModes.easy_mode(select, mode)
                break
            elif mode.lower() == "medium":
                GameModes.main_mode(select, mode, gen_select)
                # print("placeholder")
                break
            elif mode.lower() == "hard":
                # GameModes.hard_mode(select)
                print("placeholder")
                break
            else:
                print("incorrect")


# runPokeGuesser()
# a = list(range(1, 807))
# shuffle(a)
# a[0] = 1
# GameModes.main_mode(a, "easy")
if __name__ == "__main__":
    setup()
