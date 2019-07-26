import argparse
import pandas
import csv
import numpy as np


def create_histogram(input_file, output_file):
    reader=pandas.read_csv(input_file, iterator=True, header=None)
    datamin = -1
    datamax = 1
    delimeters = 21
    mybins = np.linspace(datamin, datamax, delimeters)
    hist = np.zeros(delimeters-1, dtype='int32')
    for chunk in reader:
        htemp, junk = np.histogram(chunk, mybins)
        hist += htemp
    with open(output_file, 'w') as out:
        writer = csv.writer(out)
        writer.writerow(hist)

def main():
    parser = argparse.ArgumentParser(description='parse arguments')
    parser.add_argument('input_file', type=str, help='input file')
    parser.add_argument('output_file', type=str,)
    args = parser.parse_args()
    create_histogram(args.input_file, args.output_file)

if __name__== "__main__":
  main()
