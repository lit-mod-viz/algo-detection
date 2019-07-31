import argparse
import numpy as np
import pandas as pd
import csv

def get_indices_and_values(matrix_file, thresh):
    data = np.loadtxt(matrix_file)

    values = data[data>thresh]
    index1, index2 = np.nonzero(data>thresh)
    # indices = np.vstack((index1, index2))
    # coordinates = np.swapaxes(indices, 0, 1)
    return index1, index2, values

def get_sentences(source_file, comp_file, index1, index2):
    source_df = pd.read_csv(source_file,sep='\n', header=None)
    comp_df = pd.read_csv(comp_file,sep='\n', header=None)

    source_sents = source_df.ix[index1].values.flatten()
    comp_sents = comp_df.ix[index2].values.flatten()

    return source_sents, comp_sents

def write_csv(out_file, list1, list2, values):
    with open(out_file, 'w') as out:
        writer = csv.writer(out)
        header = ["Source", "Compare", "Value"]
        writer.writerow(header)
        for i, val in enumerate(values):
            row = [list1[i], list2[i], val]
            writer.writerow(row)

def main():
    parser = argparse.ArgumentParser(description='parse arguments')
    parser.add_argument('matrix_file', type=str, help='matrix file')
    parser.add_argument('source_file', type=str, help='file with source sentences used to generate matrix')
    parser.add_argument('comp_file', type=str, help='file with compare sentences used to generate matrix')
    parser.add_argument('out_file', type=str, help='file to write out to')    
    parser.add_argument('thresh', type=float, help='threshold to cull from matrix, range -1 to 1, (greater than)')
    
    args = parser.parse_args()

    index1, index2, values = get_indices_and_values(args.matrix_file, args.thresh)
    source_sents, comp_sents = get_sentences(args.source_file, args.comp_file, index1, index2)

    write_csv(args.out_file, source_sents, comp_sents, values)

if __name__== "__main__":
    main()