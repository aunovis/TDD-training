import os
import sys

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QVBoxLayout, QWidget

CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))


class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()

        self.button = QtWidgets.QPushButton("test", self)
        self.label = QtWidgets.QLabel("console output")

        widget = QWidget()
        layout = QVBoxLayout(widget)
        layout.addWidget(self.button)
        layout.addWidget(self.label)
        self.setCentralWidget(widget)

        self.process = QtCore.QProcess()
        self.process.setProgram(sys.executable)

        self.button.clicked.connect(self.on_clicked)

        self.fs_watcher = QtCore.QFileSystemWatcher(["status.txt"])
        self.fs_watcher.fileChanged.connect(self.on_file_changed)

    @QtCore.pyqtSlot()
    def on_clicked(self):
        self.process.setWorkingDirectory(CURRENT_DIR)
        self.process.setArguments(["-m", "pytest", "-s"])
        self.process.start()

    @QtCore.pyqtSlot()
    def on_file_changed(self):
        with open('status.txt', 'rb') as f:
            f.seek(-2, os.SEEK_END)
            while f.read(1) != b'\n':
                f.seek(-2, os.SEEK_CUR)
            last_line = f.readline().decode()
        self.label.setText(last_line)
