import os
import sys

from pathlib import Path

from PyQt5.QtWidgets import QApplication, QComboBox, QLabel, QMainWindow, QPushButton
from PyQt5 import uic


class PlanBAI(QMainWindow):
    def __init__(self):
        # Override
        super(PlanBAI, self).__init__()

        # Load UI
        self.load_ui()

        # Define/connect our widgets
        self.serialPortCombo = self.findChild(QComboBox, "serialPortComboBox")
        self.serialConnectionLabel = self.findChild(QLabel, "serialConnectionLabel")
        self.serialConnectButton = self.findChild(QPushButton, "serialConnectButton")

        self.serialPortCombo.addItem("/dev/ttyACM0") # Move me somehwere else

        # Attach buttons/functions
        self.serialConnectButton.clicked.connect(self.connectArduino)

        # Show the UI
        self.show()

    def load_ui(self):
        path = os.fspath(Path(__file__).resolve().parent / "resources/planb.ui")  # NOQA: E501

        # Load UI frompath
        uic.loadUi(path, self)

    def connectArduino(self):
        self.serialConnectionLabel.setText("Starting Connection attempt...")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    UIWindow = PlanBAI()
    app.exec_()
