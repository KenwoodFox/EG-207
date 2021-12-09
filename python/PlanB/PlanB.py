import os
import sys
import time
from PyQt5.QtGui import QTextBlock
import serial
import pyqtgraph as pg

from pathlib import Path

from PyQt5.QtWidgets import QAction, QApplication, QComboBox, QLabel, QMainWindow, QPushButton, QTextEdit
from PyQt5 import uic
from pyqtgraph import PlotWidget, plot
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

        self.serialLog = self.findChild(QTextEdit, "serialLogWindow")
        
        self.exitCleanlyDropdown = self.findChild(QAction, "actionExit_Cleanly")

        self.graphWidget = self.findChild(PlotWidget, "mainGraph")

        self.serialPortCombo.addItem("/dev/ttyACM0") # Move me somehwere else

        # Attach buttons/functions
        self.serialConnectButton.clicked.connect(self.connectArduino)
        self.exitCleanlyDropdown.triggered.connect(self.exitCleanly)

        # Style our graphs
        hour = [1,2,3,4,5,6,7,8,9,10]
        temperature_1 = [30,32,34,32,33,31,29,32,35,45]
        temperature_2 = [5.0,3.5,4.4,2.2,3.8,3.2,2.7,3.8,3.2,4.4]

        # Set background color to white.
        self.graphWidget.setBackground('w')

        # Add Title
        self.graphWidget.setTitle("Climate Air Conditions", color="b", size="16pt")

        # Add Axis Labels
        tempStyle = {"color": "#f00", "font-size": "20px"}
        humidityStyle = {"color": "#00f", "font-size": "20px"}
        self.graphWidget.setLabel("left", "Temperature (°C)", **tempStyle)
        self.graphWidget.setLabel("right", "Humidity (Rh%)", **humidityStyle)
        self.graphWidget.setLabel("bottom", "Hour (H)", **tempStyle)

        # Add legend
        self.graphWidget.addLegend()

        # Add grid
        self.graphWidget.showGrid(x=True, y=True)

        # Set Range
        # self.graphWidget.setXRange(0, 4, padding=0)  # Last four hours
        #self.graphWidget.setYRange(-10, 70, padding=0)

        self.plot(hour, temperature_1, "Temp", 'r')
        self.plot(hour, temperature_2, "Humidity", 'b')


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
            self.arduino = serial.Serial(self.serialPortCombo.currentText(),
                                         115200,
                                         timeout=1)
        except SerialException:
            self.serialConnectionLabel.setText("Connection Error.")

        self.serialConnectionLabel.setText("Please wait...")
        self.serialConnectionLabel.repaint()
        self.show()
        time.sleep(5)

        # Write v to check for arduino version
        self.arduino.write("v".encode())

        self.arduino_ver = self.logRead()
        self.serialConnectionLabel.setText(f"Connected! Version is {self.arduino_ver}.")

    def plot(self, x, y, plotname, color):
        pen = pg.mkPen(color=color)
        self.graphWidget.plot(x, y, name=plotname, pen=pen, symbolSize=3, symbolBrush=(color))

    def logRead(self, initmode=False):
        # Reads a line and decodes it but also prints it out to the 'console' window.
        line = str(self.arduino.readline().decode().strip('\n\r'))

        self.serialLog.append(line)
        self.serialLog.verticalScrollBar().setValue(self.serialLog.verticalScrollBar().maximum())

        return line

    def exitCleanly(self):
        self.arduino.close()
        quit()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    UIWindow = PlanBAI()
    app.exec_()
