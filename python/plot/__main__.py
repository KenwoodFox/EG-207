import time
import serial
import logging

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib as mpl

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
ax.tick_params(labelcolor='w', top=False, bottom=False, left=False, right=False)

ax.set_xlabel('Time (Epoch)')

temp_line_plot.set_title('Temp')
humidity_line_plot.set_title('Humidity')


def animate(i, arduino):
    try:
        # Frame is one data frame
        frame = arduino.readline().decode().strip('\n')

        # Split up frame
        frame = frame.split(',')

        humidy = frame[0].strip('H')
        temp = frame[1].strip('T')

        # Logging
        print(f'Got new frame: {frame}')

        time_scale.append(int(time.time()))
        temp_reading.append(float(temp))
        humidity_reading.append(float(humidy))

        temp_line_plot.plot(time_scale, temp_reading, color="red")
        humidity_line_plot.plot(time_scale, humidity_reading, color="blue")

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
        ani = animation.FuncAnimation(fig, animate, fargs=[arduino], interval=100)
        plt.show()
    except KeyboardInterrupt:
        arduino.close()
        quit()
