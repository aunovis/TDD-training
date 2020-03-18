import os
import sys

from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtGui import QMovie
from PyQt5.QtWidgets import QVBoxLayout, QWidget, QHBoxLayout

CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))


class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()

        self._main = QtWidgets.QWidget()
        self.setCentralWidget(self._main)

        self.button = QtWidgets.QPushButton("Start tests")
        self.console_label = QtWidgets.QLabel("Lift output")
        self.status_label = QtWidgets.QLabel("Lift movement")
        self.pic = QtWidgets.QLabel()
        self.pic.setPixmap(QtGui.QPixmap("img\\lift_open.png"))
        self.arrow = QtWidgets.QLabel()
        self.arrow_down_gif = QMovie("img\\arrow_down.gif")
        self.arrow_up_gif = QMovie("img\\arrow_up.gif")

        layout = QtWidgets.QGridLayout(self._main)

        layout.addWidget(self.button, 0, 0)
        layout.addWidget(self.console_label, 1, 0)
        layout.addWidget(self.pic, 2, 0)
        layout.addWidget(self.status_label, 1, 1)
        layout.addWidget(self.arrow, 2, 1)

        self.process = QtCore.QProcess()
        self.process.setProgram(sys.executable)

        self.button.clicked.connect(self.on_clicked)

        self.fs_watcher = QtCore.QFileSystemWatcher(["status.txt"])
        self.fs_watcher.fileChanged.connect(self.on_file_changed)

    @QtCore.pyqtSlot()
    def on_clicked(self):
        self.process.setWorkingDirectory(CURRENT_DIR)
        self.process.setArguments(["-m", "pytest", "-s", "-k test_fast_order"])
        self.process.start()

    @QtCore.pyqtSlot()
    def on_file_changed(self):
        with open('status.txt', 'rb') as f:
            f.seek(-2, os.SEEK_END)
            while f.read(1) != b'\n':
                f.seek(-2, os.SEEK_CUR)
            last_line = f.readline().decode()
        self.console_label.setText(last_line)
        if ("Hello" in last_line) | ("opened now" in last_line):
            self.pic.setPixmap(QtGui.QPixmap("img\\lift_open.png"))
        if "closing doors" in last_line:
            self.pic.setPixmap(QtGui.QPixmap("img\\lift_closing.png"))
        if "opening doors" in last_line:
            self.pic.setPixmap(QtGui.QPixmap("img\\lift_opening.png"))
        if "DING" in last_line:
            self.arrow.hide()
            self.arrow_up_gif.stop()
            self.arrow_down_gif.stop()
            self.pic.setPixmap(QtGui.QPixmap("img\\lift_ding.png"))
        if "closed now" in last_line:
            self.pic.setPixmap(QtGui.QPixmap("img\\lift_closed.png"))
        if "Moving up" in last_line:
            self.arrow.setMovie(self.arrow_up_gif)
            self.arrow_up_gif.start()
            self.arrow.show()
        if "Moving down" in last_line:
            self.arrow.setMovie(self.arrow_down_gif)
            self.arrow_down_gif.start()
            self.arrow.show()
