import argparse
import pandas
import csv
import numpy as np


def top_sentences(input_file, output_file):
    reader=pandas.read_csv(input_file, iterator=True, header=None)
    with open(output_file, 'w') as out:
        writer = csv.writer(out)

        for i, chunk in enumerate(reader):
            for j, value in enumerate(chunk):
                if value > .9:
                    writer.writerow((i, j, value))

def main():
    parser = argparse.ArgumentParser(description='parse arguments')
    parser.add_argument('input_file', type=str, help='input file')
    parser.add_argument('output_file', type=str,)
    args = parser.parse_args()
    top_sentences(args.input_file, args.output_file)

if __name__== "__main__":
  main()
