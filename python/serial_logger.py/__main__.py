# Team Gold
# EG-207 Southern New Hampshire University

import sys
import csv
import serial


if __name__ == '__main__':
    with serial.Serial('/dev/ttyACM0', 115200, timeout=1) as arduino:
        while not KeyboardInterrupt:
            print(arduino.readline())
