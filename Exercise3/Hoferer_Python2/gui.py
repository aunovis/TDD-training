import PySimpleGUI as sg


class Gui:
    def __init__(self):
        layout = [[sg.Text('Hello World', key='blub')]]
        self.window = sg.Window('Hello world', layout).Finalize()

    def change_to(self, text):
        self.window.find_element('blub').Update(text)

    def close_gui(self):
        self.window.close()
