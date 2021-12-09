import os
import sys
import time
from PyQt5.QtCore import QThread, pyqtSignal
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
        self.time = []
        self.temperatureReading = []
        self.humidityReading = []

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

        self.plot(self.time, self.temperatureReading, "Temp", 'r')
        self.plot(self.time, self.humidityReading, "Humidity", 'b')


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

        self.arduino_ver, ack = self.logRead()
        self.serialConnectionLabel.setText(f"Connected! Version is {self.arduino_ver}.")

        # Configure polling system
        self.poller = Poller(self.arduino)
        self.poller.start()

        self.poller.update_graph.connect(self.updateGraph)

    def plot(self, x, y, plotname, color):
        pen = pg.mkPen(color=color)
        self.graphWidget.plot(x, y, name=plotname, pen=pen, symbolSize=3, symbolBrush=(color))

    def logRead(self, initmode=False):
        # Reads a line and decodes it but also prints it out to the 'console' window.
        line = str(self.arduino.readline().decode().strip('\n\r'))
        ack = str(self.arduino.readline().decode().strip('\n\r'))

        self.serialLog.append(line)
        self.serialLog.verticalScrollBar().setValue(self.serialLog.verticalScrollBar().maximum())

        return line, ack

    def updateGraph(self):
        new_value, ack = self.logRead()

    def exitCleanly(self):
        self.arduino.close()
        quit()


class Poller(QThread):
    update_graph = pyqtSignal()
    def __init__(self, _arduino):
        self.arduino = _arduino

        # Override
        super(Poller, self).__init__()


    def run(self):
        while True:
            time.sleep(2)
            print("Polling...")
            self.arduino.write("t".encode())
            self.update_graph.emit()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    UIWindow = PlanBAI()
    app.exec_()
