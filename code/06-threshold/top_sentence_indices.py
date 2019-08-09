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

def filter_sentence_length(source, compare, values):
    """
    Should return the indices and sentences
    """
    len1 = 1
    len2 = 2
    
    combined = pd.concat([source, compare], axis=1, ignore_index=True)
    source_lengths = combined.iloc[0:][0].str.split().str.len()
    compare_lengths = combined.iloc[0:][2].str.split().str.len()
    ret = combined[(source_lengths.gt(len1) & compare_lengths.gt(len2)) | (source_lengths.gt(len2) & compare_lengths.gt(len1))]
    source_ret = ret[0]
    og_s_idxs = ret[1]
    comp_ret = ret[2]
    og_c_idxs = ret[3]
    values[values[ret.index]]
    return source_ret, comp_ret, og_s_idxs, og_c_idxs

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
    parser.add_argument('og_source_file', type=str, help='file with og source sentences used to generate matrix')
    parser.add_argument('og_comp_file', type=str, help='file with og compare sentences used to generate matrix')

    args = parser.parse_args()

    source_df = get_df(args.source_file)
    comp_df = get_df(args.comp_file)

    og_source_df = get_df(args.og_source_file)
    og_comp_df = get_df(args.og_comp_file)

    source_idxs, comp_idxs, thresh_values = get_indices_and_values(args.matrix_file, args.thresh)

    thresh_source_sents = extract_from_df(source_df, source_idxs, 0)
    thresh_s_og_idxs = extract_from_df(source_df, source_idxs, 1)
    thresh_source = pd.concat([pd.DataFrame(thresh_source_sents), pd.DataFrame(thresh_s_og_idxs)], axis=1, ignore_index=True) 
    
    thresh_comp_sents = extract_from_df(comp_df, comp_idxs, 0)
    thresh_c_og_idxs = extract_from_df(comp_df, comp_idxs, 1)
    thresh_comp = pd.concat([pd.DataFrame(thresh_comp_sents), pd.DataFrame(thresh_c_og_idxs)], axis=1, ignore_index=True)

    source_sents, comp_sents, og_s_idxs, og_c_idxs, values = filter_sentence_length(thresh_source, thresh_comp, thresh_values)

    og_s_sents = extract_from_df(og_source_df, og_s_idxs, 0)
    og_c_sents = extract_from_df(og_comp_df, og_c_idxs, 0)

    sents_fp = args.out_file + ".sents.clean.thresh"
    idxs_fp = args.out_file + ".idxs.og.thresh"
    og_sents_fp = args.out_file + ".sents.og.thresh"

    write_csv(sents_fp, source_sents, comp_sents, values)
    write_csv(idxs_fp, og_s_idxs, og_c_idxs, values)
    write_csv(og_sents_fp, og_s_sents, og_c_sents, values)

if __name__== "__main__":
    main()