# Team Gold
# EG-207
# Southern New Hampshire University, 2021

import re
import csv
import time
import serial
import logging
import argparse

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib as mpl


class GoldPlotApp:
    def __init__(self, logger, **kwargs):
        # logging
        self.log = logger

        # Graph theme
        mpl.style.use('seaborn')

        # Parse args
        parser = argparse.ArgumentParser(description='Parse args.')
        parser.add_argument('--port',
                            nargs='?',
                            default='/dev/ttyACM0',
                            type=str)

        parser.add_argument('--data',
                            nargs='?',
                            default=None,
                            type=str)

        parser.add_argument('-o',
                            nargs='?',
                            default='output.csv',
                            type=str)

        self.args = parser.parse_args()

        if self.args.data is None:
            # Log
            self.log.info("Initalizing arduino.")

            # Connect arduino
            self.arduino = serial.Serial(self.args.port, 115200, timeout=1)

            # Data for this run
            self.csv_data = open(self.args.o, 'w')
            self.csv_writer = csv.writer(self.csv_data, delimiter=',',
                                         quotechar='"',
                                         quoting=csv.QUOTE_MINIMAL)
            self.csv_writer.writerow(['Epoch Time', 'Temp', 'Humidity'])

        else:
            # Load csv data instead.
            self.log.debug("Loading CSV.")
            with open(self.args.data, mode='r') as datafile:
                csv_reader = csv.DictReader(datafile)
                for row in csv_reader:
                    self.log.debug(row)
                    if row['Epoch Time'] is float:
                        self.log.debug(f"Read data frame at time {row['Epoch Time']}, with temp {row['Temp']} and humidity {row['Humidity']}")

        # Arduino version
        self.arduino_version = None
        # Setup graph
        self.initalize_graph()

    def run(self):
        if self.args.data is None:
            # Setup animated graph.
            ani = animation.FuncAnimation(self.fig,
                                          self.update_graph,
                                          interval=200)

            # Just for flake
            ani.__str__()
        else:
            self.log.debug("Got to run")

        # Show plot!
        plt.show()

    def get_new_frame(self):
        # Time
        now = float(time.time())
        # Frame is one data frame
        frame = self.arduino.readline().decode().strip('\n')

        try:
            ver_match = re.search('(?<=version )(.*)', frame).group(0)
            if ver_match is not None:
                self.arduino_version = str(ver_match)
        except AttributeError:
            pass

        try:
            if len(frame) > 0:
                # Capture a new frame
                frame = frame.split(',')
                self.log.debug(f'Raw frame is {frame}')

                self.current_humidy = float(frame[0].strip('H'))
                self.current_temp = float(frame[1].strip('T'))

                if self.current_humidy != 0 and self.current_temp != 0:
                    # Logging
                    self.log.info(f'Got new frame: {frame}')

                    # Plot scales
                    self.time_scale.append(now)
                    self.temp_reading.append(self.current_temp)
                    self.humidity_reading.append(self.current_humidy)
                else:
                    logging.error(f'Error, empty frame: {frame}')
        except (IndexError, AttributeError, ValueError):
            self.log.warn('Got bad frame')

        # Trigger a csv update
        self.write_csv()

    def write_csv(self):
        try:
            self.csv_writer.writerow([self.time_scale[-1],
                                     self.temp_reading[-1],
                                     self.humidity_reading[-1]])
        except IndexError:
            self.log.warn("Not writing bad frame to csv.")

    def initalize_graph(self):
        # Setup figure
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(111)
        self.temp_line_plot = self.fig.add_subplot(2, 1, 1)
        self.humidity_line_plot = self.fig.add_subplot(2, 1, 2)

        # Mess
        self.time_scale = []
        self.temp_reading = []
        self.max_temp = 0
        self.max_temp_time = 0
        self.humidity_reading = []
        self.current_humidy = float(0)
        self.current_temp = float(0)

        # Spacing
        self.fig.tight_layout(pad=3.0)

        # Turn off axis lines and ticks of the big subplot
        self.ax.spines['top'].set_color('none')
        self.ax.spines['bottom'].set_color('none')
        self.ax.spines['left'].set_color('none')
        self.ax.spines['right'].set_color('none')
        self.ax.tick_params(labelcolor='w',
                            top=False,
                            bottom=False,
                            left=False,
                            right=False)

        self.ax.set_xlabel('Time (Epoch)')

        self.temp_line_plot.set_title('Temp')
        self.humidity_line_plot.set_title('Humidity')

    def update_graph(self, i):
        try:
            # Time
            now = int(time.time())

            # Get new frame
            self.get_new_frame()

            self.temp_line_plot.clear()
            self.temp_line_plot.plot(self.time_scale,
                                     self.temp_reading,
                                     color="red")

            self.humidity_line_plot.clear()
            self.humidity_line_plot.plot(self.time_scale,
                                         self.humidity_reading,
                                         color="blue")

            # Annotations
            # If there is a new max
            if float(self.current_temp) > self.max_temp:
                # Save the new max
                self.max_temp = self.current_temp
                self.max_temp_time = now

            # Annotate the max
            self.temp_line_plot.annotate('Max Temp',
                                         xy=(self.max_temp_time,
                                             self.max_temp),
                                         xycoords='data',
                                         xytext=(0.2, 0.95),
                                         textcoords='axes fraction',
                                         arrowprops=dict(facecolor='black',
                                                         shrink=0.05),
                                         horizontalalignment='right',
                                         verticalalignment='top')

            plt.show()
        except KeyboardInterrupt:
            self.log.info('Exiting safely.')
            self.close()

    def close(self):
        self.log.info(f'Arduino was using version {self.arduino_version}')
        self.arduino.close()
        self.csv_data.close()
        quit()
