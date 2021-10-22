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

        # What data to use
        parser.add_argument('--data',
                            nargs='?',
                            default=None,
                            type=str)

        # The standard for this dataset
        parser.add_argument('--std',
                            nargs='?',
                            default=-1,
                            type=int)

        # Number of display bins
        parser.add_argument('-b',
                            nargs='?',
                            default=3,
                            type=int)

        # Idk
        parser.add_argument('-l',
                            action='store_true')

        # Weather or not to do the TC math
        parser.add_argument('-t',
                            action='store_true')

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
        fig, ax = plt.subplots(2)

        # Annotations/math
        mu = self.data.mean()
        median = np.median(self.data)
        mean = np.mean(self.data)
        sigma = self.data.std()
        accuracy = abs((mean - self.args.std) / mean) * 100
        percision = ((2 * sigma) / self.args.std) * 100

        max = np.amax(self.data)
        data_points_to_reach_max = np.where(self.data == max)[0][0]
        time_to_max = self.time_scale[data_points_to_reach_max] - self.time_scale[0]
        time_const = time_to_max

        # This is really messy and needs to be cleaned up!!!
        if self.args.std != -1:
            annotationtext = '\n'.join((
                r'$\mu=%.2f$' % (mu, ),
                r'$\mathrm{median}=%.2f$' % (median, ),
                r'$\sigma=%.2f$' % (sigma, ),
                r'$\mathrm{accuracy}=%.2f$' % (accuracy, ),
                r'$\mathrm{percision}=%.2f$' % (percision, )))
        elif self.args.t:
            annotationtext = '\n'.join((
                r'$\mu=%.2f$' % (mu, ),
                r'$\mathrm{median}=%.2f$' % (median, ),
                r'$\sigma=%.2f$' % (sigma, ),
                r'$\tau=%.2f$' % (time_const, )))
        else:
            annotationtext = '\n'.join((
                r'$\mu=%.2f$' % (mu, ),
                r'$\mathrm{median}=%.2f$' % (median, ),
                r'$\sigma=%.2f$' % (sigma, )))

        ax[0].annotate('Gold Standard, Team Gold, SNHU',
                         xy=(1.0, 1.25),
                         xycoords='axes fraction',
                         horizontalalignment='right',
                         verticalalignment='top')


        # Histogram plot
        ax[0].hist(self.data, bins=self.args.b)

        # Add data over time plot
        ax[1].plot(self.data)

        # add labels
        ax[0].set_xlabel('Value')
        ax[0].set_ylabel('Frequency')
        ax[1].set_xlabel('Epoch')
        ax[1].set_ylabel('Value')
        ax[0].set_title(self.args.data)

        props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)

        # place a text box in upper left in axes coords
        ax[0].text(0.05, 0.95, annotationtext, transform=ax[0].transAxes, fontsize=14,
                verticalalignment='top', bbox=props)

        plt.show()
