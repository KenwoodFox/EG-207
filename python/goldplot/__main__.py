# Team Gold
# EG-207
# Southern New Hampshire University, 2021

import time
import serial
import logging

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib as mpl


# Select plot theme
mpl.style.use('seaborn')

fig = plt.figure()
ax = fig.add_subplot(111)
temp_line_plot = fig.add_subplot(2, 1, 1, label="Temp")
humidity_line_plot = fig.add_subplot(2, 1, 2, label="Humidity")

time_scale = []
temp_reading = []
humidity_reading = []

# Spacing
fig.tight_layout(pad=3.0)

# Turn off axis lines and ticks of the big subplot
ax.spines['top'].set_color('none')
ax.spines['bottom'].set_color('none')
ax.spines['left'].set_color('none')
ax.spines['right'].set_color('none')
ax.tick_params(labelcolor='w',
               top=False,
               bottom=False,
               left=False,
               right=False)

ax.set_xlabel('Time (Epoch)')

temp_line_plot.set_title('Temp')
humidity_line_plot.set_title('Humidity')


def animate(i, arduino):
    try:
        # Time
        now = int(time.time())
        # Frame is one data frame
        frame = arduino.readline().decode().strip('\n')

        # Split up frame
        frame = frame.split(',')

        humidy = frame[0].strip('H')
        temp = frame[1].strip('T')

        # Logging
        print(f'Got new frame: {frame}')

        # Plot scales
        time_scale.append(now)
        temp_reading.append(float(temp))
        humidity_reading.append(float(humidy))

        temp_line_plot.plot(time_scale, temp_reading, color="red")
        humidity_line_plot.plot(time_scale, humidity_reading, color="blue")

        # Annotations
        # Max value
        max_temp = float(max(temp_reading))
        max_temp_time = now
        logging.info(f'max is at {max_temp_time} with value {max_temp}')

        temp_line_plot.annotate('Max Temp',
                                xy=(max_temp, now - 1),
                                xycoords='figure pixels',
                                arrowprops=dict(facecolor='black',
                                                shrink=0.05),
                                horizontalalignment='left',
                                verticalalignment='top')
        plt.show()
    except KeyboardInterrupt:
        print('Exiting safely.')
        exit()
    except IndexError:
        pass


if __name__ == '__main__':
    try:
        logging.basicConfig(level=logging.INFO)

        arduino = serial.Serial('/dev/ttyACM0', 115200, timeout=1)
        ani = animation.FuncAnimation(fig,
                                      animate,
                                      fargs=[arduino],
                                      interval=100)
        plt.show()
    except KeyboardInterrupt:
        arduino.close()
        quit()
