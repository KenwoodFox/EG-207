import os
import sys
import time
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtGui import QTextBlock
import serial
import pyqtgraph as pg

from pathlib import Path

from PyQt5.QtWidgets import QAction, QApplication, QCheckBox, QComboBox, QLabel, QMainWindow, QPushButton, QTextEdit
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

        self.enablePollingCheckbox = self.findChild(QCheckBox, "enablePollingCheckbox")

        self.serialPortCombo.addItems(["/dev/ttyACM0", "/dev/ttyACM1", "COM1", "COM5"]) # Move me somehwere else

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

        # Setup lots
        pen = pg.mkPen(color='r')
        self.tempPlot = self.graphWidget.plot(self.time, self.temperatureReading, name="Temp", pen=pen, symbolSize=3, symbolBrush=('r'))
        pen = pg.mkPen(color='b')
        self.humidityPlot = self.graphWidget.plot(self.time, self.temperatureReading, name="Humidity", pen=pen, symbolSize=3, symbolBrush=('b'))


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

            self.serialConnectionLabel.setText("Please wait...")
            self.serialConnectionLabel.repaint()
            self.show()
            time.sleep(5)

            # Write v to check for arduino version
            self.arduino.write("v".encode())

            self.arduino_ver, ack = self.logRead()
            self.serialConnectionLabel.setText(f"Connected! Version is {self.arduino_ver}.")

            # Configure polling system
            self.poller = Poller()
            self.poller.start()

            self.poller.update_graph.connect(self.updateLive)

        except SerialException:
            self.serialConnectionLabel.setText("Connection Error.")

    def logRead(self, initmode=False):
        # Reads a line and decodes it but also prints it out to the 'console' window.
        line = str(self.arduino.readline().decode().strip('\n\r'))
        ack = str(self.arduino.readline().decode().strip('\n\r'))

        self.serialLog.append(line)
        self.serialLog.verticalScrollBar().setValue(self.serialLog.verticalScrollBar().maximum())

        return line, ack

    def updateLive(self):
        # Updates anything "live onscreen"
        print("Updating graph")

        try:
            now = float(time.time())
            self.time.append(now)

            self.arduino.write("t".encode())
            new_value, ack = self.logRead()
            new_value = float(new_value.strip('T'))
            print(new_value)
            self.temperatureReading.append(new_value)

            self.arduino.write("h".encode())
            new_value, ack = self.logRead()
            new_value = float(new_value.strip('H'))
            print(new_value)
            self.humidityReading.append(new_value)

            self.tempPlot.setData(self.time, self.temperatureReading)
            self.humidityPlot.setData(self.time, self.humidityReading)
        except:
            print("Pharsing error?")


    def exitCleanly(self):
        self.arduino.close()
        quit()


class Poller(QThread):
    # Triggers stuff tied to it, has no logic
    update_graph = pyqtSignal()

    def run(self):
        while True:
            time.sleep(0.8)
            self.update_graph.emit()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    UIWindow = PlanBAI()
    app.exec_()
