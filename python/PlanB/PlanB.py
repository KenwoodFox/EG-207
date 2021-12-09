import os
import sys
import time
import serial

from pathlib import Path

from PyQt5.QtWidgets import QAction, QApplication, QComboBox, QLabel, QMainWindow, QPushButton
from PyQt5 import uic
from serial.serialutil import SerialException


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
        
        self.exitCleanlyDropdown = self.findChild(QAction, "actionExit_Cleanly")

        self.serialPortCombo.addItem("/dev/ttyACM0") # Move me somehwere else

        # Attach buttons/functions
        self.serialConnectButton.clicked.connect(self.connectArduino)
        self.exitCleanlyDropdown.triggered.connect(self.exitCleanly)

        # Show the UI
        self.show()

    def load_ui(self):
        path = os.fspath(Path(__file__).resolve().parent / "resources/planb.ui")  # NOQA: E501

        # Load UI frompath
        uic.loadUi(path, self)

    def connectArduino(self):
        self.serialConnectionLabel.setText("Starting Connection attempt...")
        self.serialConnectionLabel.repaint()

        # Connect to serial port.
        try:
            self.arduino = serial.Serial(self.serialPortCombo.currentText(), 115200, timeout=1)
        except SerialException:
            self.serialConnectionLabel.setText("Connection Error.")

        self.serialConnectionLabel.setText("Please wait...")
        self.serialConnectionLabel.repaint()
        self.show()
        time.sleep(5)

        # Write v to check for arduino version
        self.arduino.write("v".encode())

        self.arduino_ver = str(self.arduino.readline().decode().strip('\n\r'))
        self.serialConnectionLabel.setText(f"Connected! Version is {self.arduino_ver}.")
    
    def exitCleanly(self):
        self.arduino.close()
        quit()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    UIWindow = PlanBAI()
    app.exec_()
