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
                select, gen_select = self.gen_selector()
                if select and gen_select == False:
                    select, gen_select = self.gen_selector()

                print(select)
                print(gen_select)
                #self.mode_select(self.select, self.gen_select)

                # self.input.update("")
                # self.window['-OUTPUT-'].update(values["-IN-"])
                # x = r"res\\thumb-1920-574726.png"
                # self.imageElem.Update(filename=x, size=(300, 300))
                print(self.event)

    def runPokeGuesser(self):
        self.build()
        self.gen_selector()

    def gen_selector(self):
        # should describe max generations and all
        gen_select = self.values['-IN-']
        print(gen_select)
        # gen_select = input("Welcome message. Select generation, gen 1 -7 or All\n")
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
                return False, False

        self.select = [int]

        for i in range(lower_bind, upper_bind + 1):
            self.select.append(i)

        shuffle(self.select)

        self.introMessage.Update(gen_select.capitalize() + " Selected: ")

        return self.select, gen_select,  # probably redundant

    def mode_select(self, select, gen_select):
        while 1 < 2:
            self.introMessage.Update("Now select a mode, easy medium, hard\n")
            # describe modes here
            mode = self.values['-IN-']
            print(mode)
            if mode.lower() == "easy" or "medium" or "hard":
                GameModes.main_mode(self.select, mode, self.gen_select)
            else:
                self.introMessage.Update("invalid entry detected")


# runPokeGuesser()
# a = list(range(1, 807))
# shuffle(a)
# a[0] = 1
# GameModes.main_mode(a, "easy")
if __name__ == "__main__":
    setup()
