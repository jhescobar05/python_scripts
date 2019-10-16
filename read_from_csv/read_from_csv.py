
# -*- coding: utf-8 -*-

import csv
import argparse


def loadcsv(filename=None):

    # read and print contents found in csv file
    with open(filename, 'r') as f:
        reader = csv.reader(f)

        for row in reader:
            print(row)

if __name__ == '__main__':


    parser = argparse.ArgumentParser()

    parser.add_argument("-f", "--filename", type=str,
                        help="Provide csv filename.")
    args = parser.parse_args()

    if args.filename:
        outfile = loadcsv(filename=args.filename)
    else:
        raise exception("Filename was not provided.")
