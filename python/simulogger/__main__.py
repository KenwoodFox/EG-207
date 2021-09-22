# Team Gold
# EG-207 Southern New Hampshire University

import csv


from random import seed
from random import random
from datetime import datetime


def simulogger():
    '''
    Simulates logging data from a serial device,
    and stores the output as a .csv
    '''
    with open('simulated_dht_data.csv', 'w') as datafile:
        datalogger = csv.writer(datafile,
                                delimiter=',',
                                quotechar='"',
                                quoting=csv.QUOTE_MINIMAL)

        datalogger.writerow(['num', 'time', 'value'])

        for i in range(100):
            datalogger.writerow([i, datetime.now().microsecond, random() + i])


if __name__ == '__main__':
    seed(1)
    simulogger()

