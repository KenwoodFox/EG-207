# Team Gold
# EG-207
# Southern New Hampshire University, 2021

import csv
import argparse

import matplotlib.pyplot as plt
import numpy as np


class GoldHist:
    def __init__(self, logger, **kwargs):
        # logging
        self.log = logger

        # Set style
        plt.style.use('ggplot')

        # Initalize plot axies
        self.time_scale = []
        self.data = []

        # Parse args
        parser = argparse.ArgumentParser(description='Parse args.')

        parser.add_argument('--data',
                            nargs='?',
                            default=None,
                            type=str)

        parser.add_argument('--std',
                            nargs='?',
                            default=None,
                            type=int)

        parser.add_argument('-b',
                            nargs='?',
                            default=3,
                            type=int)

        self.args = parser.parse_args()

        self.log.debug("Loading CSV.")
        with open(self.args.data, mode='r') as datafile:
            csv_reader = csv.DictReader(datafile)
            for row in csv_reader:
                if isinstance(row['Epoch Time'], str):
                    _time = row["Epoch Time"]
                    _data = row["Lux Level"]

                    self.time_scale.append(float(_time))
                    self.data.append(float(_data))

        # Convert data list to np array, this does not include time tho, and should.
        self.data = np.asarray(self.data)

    def run(self):
        # Make a histogram using the data
        fig, ax = plt.subplots()

        # Annotations/math
        mu = self.data.mean()
        median = np.median(self.data)
        mean = np.mean(self.data)
        sigma = self.data.std()
        accuracy = abs((mean - self.args.std) / mean) * 100
        percision = ((2 * sigma) / self.args.std) * 100

        annotationtext = '\n'.join((
            r'$\mu=%.2f$' % (mu, ),
            r'$\mathrm{median}=%.2f$' % (median, ),
            r'$\sigma=%.2f$' % (sigma, ),
            r'$\mathrm{accuracy}=%.2f$' % (accuracy, ),
            r'$\mathrm{percision}=%.2f$' % (percision, )))

        ax.annotate('Gold Standard, Team Gold, SNHU',
                         xy=(0.9, 1.12),
                         xycoords='axes fraction',
                         horizontalalignment='right',
                         verticalalignment='top')

        # Histogram plot
        ax.hist(self.data, bins=self.args.b)

        ax.set_xlabel('Value')
        ax.set_ylabel('Frequency')
        ax.set_title(self.args.data)

        props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)

        # place a text box in upper left in axes coords
        ax.text(0.05, 0.95, annotationtext, transform=ax.transAxes, fontsize=14,
                verticalalignment='top', bbox=props)

        plt.show()
