# Team Gold
# EG-207
# Southern New Hampshire University, 2021

import re
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

        # Graphing
        # Select theme
        mpl.style.use('seaborn')

        # Arduino version
        self.arduino_version = None

        # Setup graph
        self.initalize_graph()

    def run(self):
        parser = argparse.ArgumentParser(description='Parse args.')
        parser.add_argument('--port',
                            nargs='?',
                            default='/dev/ttyACM0',
                            type=str)

        args = parser.parse_args()

        self.arduino = serial.Serial(args.port, 115200, timeout=1)
        ani = animation.FuncAnimation(self.fig,
                                      self.update_graph,
                                      interval=200)

        # Just for flake
        ani.__str__()

        # Show plot!
        plt.show()

    def get_new_frame(self):
        # Time
        now = int(time.time())
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
                                         xytext=(0.8, 0.95),
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
        quit()
