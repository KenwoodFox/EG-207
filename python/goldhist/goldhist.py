# Team Gold
# EG-207
# Southern New Hampshire University, 2021

import csv
import argparse
import subprocess

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

        # TC Cuttoff value
        parser.add_argument('--tcut',
                            nargs='?',
                            default=0,
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

        # Get version
        self.software_version = self.get_git_revision_hash()

    def run(self):
        # Make a histogram using the data
        fig, ax = plt.subplots(2)

        # Annotations/math
        mu = self.data.mean()
        median = np.median(self.data)
        mean = np.mean(self.data)
        sigma = self.data.std()
        accuracy = abs((mean - self.args.std) / self.args.std) * 100
        percision = ((2 * sigma) / self.args.std) * 100

        max = np.amax(self.data)
        self.log.info(f"Found data max: {max}")

        # Time to max
        data_points_to_reach_max = np.where(self.data == max)[0][0]
        self.log.info(f"It took {data_points_to_reach_max} data points to reach max.")
        time_to_max = self.time_scale[data_points_to_reach_max] - self.time_scale[0]

        # Need to find the time it takes to get to 60% of the max value
        data_points_to_1_tau = int(data_points_to_reach_max * 0.6) # This is a bad estimate...
        self.log.info(f"It took {data_points_to_1_tau} data points to reach one tau.")
        time_to_1st_tau = self.time_scale[data_points_to_1_tau] - self.time_scale[0]

        # Tau duration minus leading 'tail' before delta env, user specified! messy!
        normalized_tau = time_to_1st_tau - (self.time_scale[self.args.tcut] - self.time_scale[0])

        time_const = normalized_tau

        # This is really messy and needs to be cleaned up!!!
        if self.args.std != -1:
            annotationtext = '\n'.join((
                r'$\mu=%.2f$' % (mu, ),
                r'$\mathrm{median}=%.2f$' % (median, ),
                r'$\sigma=%.2f$' % (sigma, ),
                r'$\mathrm{accuracy}=%.2f$' % (accuracy, ),
                r'$\mathrm{percision}=%.2f$' % (percision, )))

            ax[0].annotate(f'Std value: {self.args.std}',
                            xy=(1.0, 0.8),
                            xycoords='axes fraction',
                            horizontalalignment='right',
                            verticalalignment='top')
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

        ax[0].annotate(f'Gold Standard, Team Gold, SNHU\nVersion: {self.software_version}',
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

    def get_git_revision_hash(self) -> str:
        return subprocess.check_output(['git', 'describe', '--dirty', '--abbrev=4', '--always', '--tags']).decode('ascii').strip()  # Noqa: E501

    def find_nearest(self, list, target):
        normalized_list = []

        for element in list:
            element = abs(target - element)
            normalized_list.append(element)

        local_min = 10
        for element in normalized_list:
            if element < local_min:
                local_min = element

        index_of_min = normalized_list.index(local_min)
        return index_of_min
