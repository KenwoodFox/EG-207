# Team Gold
# EG-207 Southern New Hampshire University

import csv
import sys


from random import seed
from random import random
from datetime import datetime


def simulogger(filename):
    '''
    Simulates logging data from a serial device,
    and stores the output as a .csv
    '''
    with open(filename, 'w') as datafile:
        datalogger = csv.writer(datafile,
                                delimiter=',',
                                quotechar='"',
                                quoting=csv.QUOTE_MINIMAL)

        datalogger.writerow(['num', 'time', 'value'])

        for i in range(100):
            rand = random()
            if (rand % 2 == 0):
                rand = rand * -1

            value = round(50 + rand, 2)
            timestamp = round(datetime.now().microsecond, 2)

            datalogger.writerow([i, timestamp, value])


if __name__ == '__main__':
    seed(1)

    try:
        arg = sys.argv[1]
    except IndexError:
        print('Please include a filename.')
        exit()

    simulogger(f'{arg}.csv')
