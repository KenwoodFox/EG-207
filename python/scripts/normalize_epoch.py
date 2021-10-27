# Team Gold
# EG-207
# Southern New Hampshire University, 2021

# Simple script to normalize EPOCH Values in existing data.

import csv
import argparse

from pathlib import Path


parser = argparse.ArgumentParser(description='Parse args.')

parser.add_argument('--data',
                    nargs='?',
                    default=None,
                    type=str)

args = parser.parse_args()

start_time = None

with open(args.data, 'r', newline='') as inputFile, open(args.data + '.tmp', 'w', newline='') as writerFile:
    read_file = csv.reader(inputFile)
    write_file = csv.writer(writerFile)


    for row in read_file:
        try:
            if start_time is None:
                start_time = float(row[0]) # Set starting time

            row[0] = float(row[0]) - start_time

            write_file.writerow(row)
        except ValueError:
            print("Got header or bad value")
            write_file.writerow(row)

Path(args.data + '.tmp').rename(args.data)
