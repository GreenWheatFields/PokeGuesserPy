# values=sg.theme_list(), size=(90, 12), key='-LIST-', enable_events=True)],
import PySimpleGUI as sg
import PokeStats


class mainWindow():
    def __init__(self):
        self.imLocation = r"res\\16627.png"
        self.imageElem = sg.Image(filename=self.imLocation, key='SHOW', size=(300, 300))
        self.message = "AAAAAAAAAAAAAAAAAAAAAA"
        self.input = sg.InputText(key='-IN-', size=(90, 12), do_not_clear=False)

        self.layout = [[self.imageElem, sg.Text(self.message, size=(15, 15), key='-OUTPUT0-')],
                  [sg.Text('Your typed chars appear here:'), sg.Text(size=(15, 1), key='-OUTPUT-')],
                  [self.input],
                  [sg.Button('Show', bind_return_key=True), sg.Button('Exit')],
                  ]
        self.window = sg.Window('PokeGuesser', self.layout)

        sg.theme('BluePurple')

    def eventLoop(self):
        while True:
            event, values = self.window.read()
            print(event, values)
            if event in (None, 'Exit'):
                self.window.close()
                break
            if event == 'Show':
                # Update the "output" text element to be the value of "input" element
                self.input.update("")
                self.window['-OUTPUT-'].update(values["-IN-"])
                x = r"res\\thumb-1920-574726.png"
                self.imageElem.Update(filename=x, size=(300, 300))
                print(event)


mainWindow().eventLoop()
