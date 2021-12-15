import os
import sys
import csv
import time
import serial
import logging
import coloredlogs
import pyqtgraph as pg

from io import StringIO

from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtGui import QTextBlock


from pathlib import Path

from PyQt5.QtWidgets import (
    QAction,
    QApplication,
    QCheckBox,
    QComboBox,
    QLabel,
    QMainWindow,
    QMessageBox,
    QProgressBar,
    QPushButton,
    QSpinBox,
    QTextEdit,
)
from PyQt5 import uic
from pyqtgraph import PlotWidget, plot
from serial.serialutil import SerialException


class PlanBAI(QMainWindow):
    def __init__(self):
        # Override
        super(PlanBAI, self).__init__()

        # Create and setup a logger
        self.log = logging.getLogger(__name__)
        coloredlogs.install(level="DEBUG")  # Setup coloredlogs

        # Stuff
        self.last_error = 0
        self.last_warning = 0
        self.last_warnings_check = 0
        self.photosensor_last = 0
        self.photosensor_enable_time = 0

        # Load UI
        self.load_ui()

        # Define/connect our widgets
        self.serialPortCombo = self.findChild(QComboBox, "serialPortComboBox")
        self.serialConnectionLabel = self.findChild(
            QLabel, "serialConnectionLabel"
        )
        self.serialConnectButton = self.findChild(
            QPushButton, "serialConnectButton"
        )

        self.serialLog = self.findChild(QTextEdit, "serialLogWindow")

        self.exitCleanlyDropdown = self.findChild(
            QAction, "actionExit_Cleanly"
        )

        self.graphWidget = self.findChild(PlotWidget, "mainGraph")

        self.enablePollingCheckbox = self.findChild(
            QCheckBox, "enablePollingCheckbox"
        )

        self.enableLightSensorCheckbox = self.findChild(
            QCheckBox, "enablePhotoCheckbox"
        )

        self.photosensorCheckDuration = self.findChild(
            QSpinBox, "timeBetweenPollsSpinbox"
        )

        self.flashPhotoCoefsButton = self.findChild(
            QPushButton, "lightSensorCoefFlashButton"
        )
        self.flashPhotoCoefsStatus = self.findChild(
            QLabel, "lightSensorFlashStatus"
        )

        self.factoryDefaultsButton = self.findChild(
            QPushButton, "factoryDefaultsButton"
        )
        self.factoryDefaultsStatus = self.findChild(
            QLabel, "factoryDefaultsLabel"
        )

        self.openLightSensorDoorButton = self.findChild(
            QPushButton, "openLightSensorDoorButton"
        )
        self.closeLightSensorDoorButton = self.findChild(
            QPushButton, "closeLightSensorDoorButton"
        )

        self.flowSensorUtilBar = self.findChild(
            QProgressBar, "waterFlowRateBar"
        )

        self.streamToFileDropdown = self.findChild(QAction, "actionSave_CSV")

        self.serialPortCombo.addItems(
            ["/dev/ttyACM0", "/dev/ttyACM1", "COM1", "COM5"]
        )  # Move me somewhere else

        # Attach buttons/functions
        self.serialConnectButton.clicked.connect(self.connectArduino)
        self.exitCleanlyDropdown.triggered.connect(self.exitCleanly)
        self.streamToFileDropdown.triggered.connect(self.streamDataToFile)
        self.flashPhotoCoefsButton.clicked.connect(self.flashPhotoCoefs)
        self.factoryDefaultsButton.clicked.connect(self.flashDefaults)

        self.openLightSensorDoorButton.clicked.connect(
            self.openLightSensorDoor
        )
        self.closeLightSensorDoorButton.clicked.connect(
            self.closeLightSensorDoor
        )

        # Style our graphs
        self.time = []
        self.temperatureReading = []
        self.humidityReading = []

        # Set background color to white.
        self.graphWidget.setBackground("w")

        # Add Title
        self.graphWidget.setTitle(
            "Climate Air Conditions", color="b", size="16pt"
        )

        # Add Axis Labels
        tempStyle = {"color": "#f00", "font-size": "20px"}
        humidityStyle = {"color": "#00f", "font-size": "20px"}
        self.graphWidget.setLabel("left", "Temperature (°C)", **tempStyle)
        self.graphWidget.setLabel("right", "Humidity (Rh%)", **humidityStyle)
        self.graphWidget.setLabel("bottom", "Epoch (s)", **tempStyle)

        # Add legend
        self.graphWidget.addLegend()

        # Add grid
        self.graphWidget.showGrid(x=True, y=True)

        # Setup plots
        pen = pg.mkPen(color="r")
        self.tempPlot = self.graphWidget.plot(
            self.time,
            self.temperatureReading,
            name="Temp",
            pen=pen,
            symbolSize=3,
            symbolBrush=("r"),
        )
        pen = pg.mkPen(color="b")
        self.humidityPlot = self.graphWidget.plot(
            self.time,
            self.temperatureReading,
            name="Humidity",
            pen=pen,
            symbolSize=3,
            symbolBrush=("b"),
        )

        # Create tempfiles
        self.temp_data = StringIO()

        self.log.info("Program started!")

        # Show the UI
        self.show()

    def load_ui(self):
        path = os.fspath(
            Path(__file__).resolve().parent / "resources/planb.ui"
        )  # NOQA: E501

        # Load UI frompath
        uic.loadUi(path, self)

    def openLightSensorDoor(self):
        self.arduino.write("=".encode())
        self.arduino.read_all()

    def closeLightSensorDoor(self):
        self.arduino.write("_".encode())
        self.arduino.read_all()

    def warningMessage(self, error_code):
        # Setup popup message box (for errors)
        self.warning_msg_box = QMessageBox()
        self.warning_msg_box.setIcon(QMessageBox.Warning)
        self.warning_msg_box.setText("Sensor reported an warning!")
        self.warning_msg_box.setInformativeText(
            f"Sensor reported an warning code {error_code}"
        )
        self.warning_msg_box.setWindowTitle("CMS Warning")
        self.warning_msg_box.setDetailedText("Details here..")
        self.warning_msg_box.setStandardButtons(
            QMessageBox.Ok | QMessageBox.Cancel
        )
        self.warning_msg_box.buttonClicked.connect(self.clear_warnings)

        self.warning_msg_box.exec_()

    def clear_warnings(self):
        self.arduino.write("W".encode())

    def errorMessage(self, error_code):
        # Setup popup message box (for errors)
        self.warning_msg_box = QMessageBox()
        self.warning_msg_box.setIcon(QMessageBox.Critical)
        self.warning_msg_box.setText("Sensor reported an error!")
        self.warning_msg_box.setInformativeText(
            f"Sensor reported an error code {error_code}"
        )
        self.warning_msg_box.setWindowTitle("CMS Error")
        self.warning_msg_box.setDetailedText("Details here..")
        self.warning_msg_box.setStandardButtons(
            QMessageBox.Ok | QMessageBox.Cancel
        )
        self.warning_msg_box.buttonClicked.connect(self.clear_errors)

        self.warning_msg_box.exec_()

    def clear_errors(self):
        self.arduino.write("E".encode())

    def connectArduino(self):
        self.serialConnectionLabel.setText("Starting Connection attempt...")
        self.serialConnectionLabel.repaint()

        # Connect to serial port.
        try:
            self.arduino = serial.Serial(
                self.serialPortCombo.currentText(), 115200, timeout=1
            )

            self.serialConnectionLabel.setText("Please wait...")
            self.serialConnectionLabel.repaint()
            self.show()
            time.sleep(5)

            # Write v to check for arduino version
            self.arduino.write("v".encode())

            self.arduino_ver, ack = self.logRead()
            self.serialConnectionLabel.setText(
                f"Connected! Version is {self.arduino_ver}."
            )

            # Configure polling systems
            self.poller = Poller()
            self.poller.start()
            self.poller.update_graph.connect(self.dataStreamer)

            # This is to offset plots and time graphs, starts when the arduino connects
            self.inital_epoch = float(time.time())

        except SerialException:
            self.serialConnectionLabel.setText("Connection Error.")

    def dataStreamer(self):
        """
        Streams data from the arduino, replaces updateLive.
        """

        # Get the current time
        now = float(time.time())

        self.log.debug("Checking for arduino stuff...")

        # Check if polling is even enabled.
        if self.enablePollingCheckbox.isChecked():
            # Query for a streamer string
            self.arduino.write("S".encode())
            try:
                line, ack = self.logRead()
                self.log.debug(f"Got a new packet! {line}, ack was {ack}.")
            except IndexError:
                self.log.warn(f"Skipping a packet, could not split {line}")

            # If line valid, send to csv
            if type(float(line.split(",")[1])) is float:
                self.temp_data.write(line)

            spamreader = csv.reader(self.temp_data, delimiter=",")
            for row in spamreader:
                print(", ".join(row))

            # Update 'live' sensors
            if ack:
                try:
                    _value = int(float(line.split(",")[5]))
                    self.flowSensorUtilBar.setValue(_value)

                    _value = float(line.split(",")[1])
                    self.temperatureReading.append(_value)

                    _value = float(line.split(",")[2])
                    self.humidityReading.append(_value)

                    now = float(time.time())
                    self.time.append(now - self.inital_epoch)

                    self.tempPlot.setData(self.time, self.temperatureReading)
                    self.humidityPlot.setData(self.time, self.humidityReading)

                    # Truncate list (this is tunable)
                    if len(self.time) > 50:
                        self.temperatureReading.pop(0)
                        self.humidityReading.pop(0)
                        self.time.pop(0)
                except IndexError:
                    self.log.warn(
                        "Could not update live sensors with this frame."
                    )

            # Schedule checking for warnings
            if self.last_warnings_check < now - 10:
                self.log.debug("Checking for warnings/errors...")
                self.checkWarnings()
                self.last_warnings_check = now

            # Schedule checking for photosensors
            if self.enableLightSensorCheckbox.isChecked():
                if (
                    self.photosensor_last
                    < now - self.photosensorCheckDuration.value()
                ):
                    self.log.debug("Enabling the photosensors.")
                    self.arduino.write("=".encode())
                    self.logRead()
                    self.photosensor_last = now
                    self.photosensor_enable_time = now

                if self.photosensor_enable_time < now - 5:
                    self.log.debug("Disabling the photosensors.")
                    self.arduino.write("_".encode())
                    self.logRead()
                    self.photosensor_enable_time = now

    def checkWarnings(self):
        # Update warnings in the background
        self.arduino.write("w".encode())
        try:
            new_value, ack = self.logRead()
            new_value = int(new_value)

            if new_value != 0 and new_value != self.last_warning:
                # If there is an error
                print(
                    f"new value is {new_value} and its different "
                    + "than the old value {self.last_warning}, "
                    + "updating diag box"
                )
                self.last_warning = new_value
                self.warningMessage(new_value)
        except ValueError:
            print("Could not read error code, idk")

        # Update errors in the background
        self.arduino.write("e".encode())
        try:
            new_value, ack = self.logRead()
            new_value = int(new_value)
            if (
                new_value != 0 and new_value != self.last_error
            ):  # If there is an error
                print(
                    f"new value is {new_value} and its different "
                    + "than the old value {self.last_error}, updating diag box"
                )
                self.last_error = new_value
                self.errorMessage(new_value)
        except ValueError:
            print("Could not read error code, idk")

    def logRead(self, check_ack=True):
        """
        Reads a line and decodes it but
        also prints it out to the 'console' window.
        """

        line = str(self.arduino.readline().decode().strip("\n\r"))
        if check_ack:
            ack = str(self.arduino.readline().decode().strip("\n\r"))
        else:
            ack = True

        self.serialLog.append(line)
        self.serialLog.verticalScrollBar().setValue(
            self.serialLog.verticalScrollBar().maximum()
        )

        return line, ack

    def updateLive(self):
        # Updates anything "live onscreen"
        print("Updating graph")

        try:
            now = float(time.time())
            self.time.append(now)

            self.arduino.write("t".encode())
            new_value, ack = self.logRead()
            new_value = float(new_value.strip("T"))
            # print(new_value)
            self.temperatureReading.append(new_value)

            self.arduino.write("h".encode())
            new_value, ack = self.logRead()
            new_value = float(new_value.strip("H"))
            # print(new_value)
            self.humidityReading.append(new_value)

            self.tempPlot.setData(self.time, self.temperatureReading)
            self.humidityPlot.setData(self.time, self.humidityReading)
        except ValueError:
            print("Phrasing error?")

        # Update long sensors here
        if self.check_long_sensors:
            if self.enableLightSensorCheckbox.isChecked() is True:
                self.arduino.write("=".encode())
                time.sleep(4)
                self.arduino.write("_".encode())

        # Update warnings in the background
        self.arduino.write("w".encode())
        try:
            new_value, ack = self.logRead()
            new_value = int(new_value)

            if new_value != 0 and new_value != self.last_warning:
                # If there is an error
                print(
                    f"new value is {new_value} and its different "
                    + "than the old value {self.last_warning}, "
                    + "updating diag box"
                )
                self.last_warning = new_value
                self.warningMessage(new_value)
        except ValueError:
            print("Could not read error code, idk")

        # Update errors in the background
        self.arduino.write("e".encode())
        try:
            new_value, ack = self.logRead()
            new_value = int(new_value)
            if (
                new_value != 0 and new_value != self.last_error
            ):  # If there is an error
                print(
                    f"new value is {new_value} and its different "
                    + "than the old value {self.last_error}, updating diag box"
                )
                self.last_error = new_value
                self.errorMessage(new_value)
        except ValueError:
            print("Could not read error code, idk")

        self.arduino.read_all()  # Flush all

    def flashPhotoCoefs(self):
        self.flashPhotoCoefsStatus.setText("No implementation.")

    def flashDefaults(self):
        self.arduino.write("D".encode())

        junk, ack = self.logRead()

        if ack == "ok":
            self.factoryDefaultsStatus.setText("Flashed!")

    def streamDataToFile(self):
        # This is messy but, its the last thing on the list.
        self.longpoller.quit()
        self.arduino.write(
            "s".encode()
        )  # Unit has to be reset to leave streaming mode...
        self.arduino.write("=".encode())
        self.datafile = open("data.csv", "w")
        self.datafile.write(
            "Epoch Time,Temperature (C), Humidity (Rh), Lux"
            + " (AVG), UV Index (AVG), Rainflow (Cubic inches per minute)"
        )  # Write header

    def superstreamer(self):
        # Idk anymore
        line, ack = self.logRead(False)

        line = line.replace("%time", str(time.time())) + "\n"

        print(line)

        self.datafile.write(line)

    def exitCleanly(self):
        self.arduino.write("_".encode())
        try:
            self.datafile.close()
            self.arduino.close()
        except AttributeError:
            pass
        quit()


class Poller(QThread):
    # Triggers stuff tied to it, has no logic
    update_graph = pyqtSignal()

    def run(self):
        while True:
            time.sleep(0.1)
            self.update_graph.emit()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    UIWindow = PlanBAI()
    app.exec_()
