import sys
import time

from PyQt5.QtWidgets import QApplication

from gui import Gui


def init_gui():
    app = QApplication(sys.argv)
    window = Gui()
    window.show()
    sys.exit(app.exec_())


def append_new_line(file_name, text_to_append):
    with open(file_name, "a+") as file_object:
        file_object.seek(0)
        data = file_object.read(100)
        if len(data) > 0:
            file_object.write("\n")
        file_object.write(text_to_append)


def give_status(text):
    time.sleep(0)
    append_new_line("status.txt", "Lifty: " + text)
    print(text)


if __name__ == "__main__":
    init_gui()
