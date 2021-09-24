# Team Gold
# EG-207 Southern New Hampshire University

import sys
import csv
import serial


if __name__ == '__main__':

    myframe = 'H39.00,T31.80,\n'
    print(myframe)
    print(myframe.split(','))

    with serial.Serial('/dev/ttyACM0', 115200, timeout=1) as arduino:
        while True:
            try:
                # Frame is one data frame
                frame = arduino.readline()

                # Split up frame
                frame = frame.split(',')

                humidy = frame[0]
                temp = frame[1]

                # Logging
                print(f'Got new frame: {frame}')
            except KeyboardInterrupt:
                print('Exiting safely.')
                exit()
