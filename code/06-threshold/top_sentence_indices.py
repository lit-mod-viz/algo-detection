import argparse
import numpy as np
import pandas as pd
import csv

def get_indices_and_values(matrix_file, thresh):
    data = pd.read_csv(matrix_file, sep=',', header=None)
    data = data.values
    values = data[data>thresh]
    source_idxs, comp_idxs = np.nonzero(data>thresh)
    # indices = np.vstack((index1, index2))
    # coordinates = np.swapaxes(indices, 0, 1)
    return source_idxs, comp_idxs, values

def get_df(fp):
    return(pd.read_csv(fp,sep=',', header=None))

def extract_from_df(df, indices, column):
    """
    returns the values of the specified column for a set of indices in the df
    column: 0 for sentences; 1 for the original indices
    """
    return(df.iloc[indices][column].values.flatten())

def write_csv(out_file, list1, list2, values):
    with open(out_file, 'w') as out:
        writer = csv.writer(out)
        header = ["Source Index", "Source Sentence", "Compare Index" "Compare Sentence", "Value"]
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
    parser.add_argument('og_sent', type=bool, help='whether or not we are getting original sentences')    
    parser.add_argument('og_indices_file', type=bool, help='if og = true: read; else: write')    

    args = parser.parse_args()

    source_df = get_df(args.source_file)
    comp_df = get_df(args.comp_file)

    if not args.og_sent:
        source_idxs, comp_idxs, values = get_indices_and_values(args.matrix_file, args.thresh)
        og_s_idxs = extract_from_df(source_df, source_idxs, 1)
        og_c_idxs = extract_from_df(comp_df, comp_idxs, 1)
        
    else:
        source_idxs, comp_idxs, values = get_df(args.og_indices_file)

    source_sents = extract_from_df(source_df, source_idxs, 0)
    comp_sents = extract_from_df(comp_df, source_idxs, 0)

    if not args.og:
        write_csv(args.og_indices_file, og_s_idxs, og_c_idxs, values)

    write_csv(args.out_file, source_sents, comp_sents, values)

if __name__== "__main__":
    main()