# Team Gold
# EG-207 Southern New Hampshire University

import sys

import matplotlib.pyplot as plt

import pandas as pd


if __name__ == '__main__':
    try:
        arg = sys.argv[1]
    except IndexError:
        print('Please include a filename.')
        exit()

    msft = pd.read_csv(arg)

    fig, ax = plt.subplots()
    msft.value_counts().plot(ax=ax, kind='bar')

    plt.show()
