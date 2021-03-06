import argparse
import numpy as np
import pandas as pd
import csv


def combine_and_weight(pcw2v, jac):
    # The values of .75 and .25 were experimentally determined on a tuning set
    newpc = pcw2v.mul(.75, 1)
    newjac = jac.mul(.25, 1)
    combined = newjac.add(newpc, fill_value=0)
    return combined

def get_indices_and_values(data, thresh):
    data = data.values
    values = data[data>thresh]
    source_idxs, comp_idxs = np.nonzero(data>thresh)
    # indices = np.vstack((index1, index2)
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
    compare_lengths = combined.iloc[0:][3].str.split().str.len()
    ret = combined[(source_lengths.gt(len1) & compare_lengths.gt(len2))]
    source_ret = ret[0]
    og_s_idxs = ret[1]
    s_idxs = ret[2]
    comp_ret = ret[3]
    og_c_idxs = ret[4]
    c_idxs = ret[5]
    ret_vals = values[ret.index]
    return source_ret, comp_ret, og_s_idxs, og_c_idxs, s_idxs, c_idxs, ret_vals

def values_at_indices(matrix, source_idxs, comp_idxs):
    """
    params:
    matrix should be a numpy array
    """
    ret = []
    for i,j in zip(source_idxs, comp_idxs):
        ret.append(matrix[i,j])
    return ret

def write_csv(out_file, list1, list2, values, values3):
    with open(out_file, 'w') as out:
        writer = csv.writer(out)
        header = ["Source", "Compare", "Value", "Val Type 2"]
        writer.writerow(header)
        for i, val in enumerate(values):
            row = [list1[i], list2[i], val, values3[i]]
            writer.writerow(row)

def main():
    parser = argparse.ArgumentParser(description='parse arguments')
    parser.add_argument('primary_matrix', type=str, help='file with similarities you want to threshold on')
    parser.add_argument('second_matrix', type=str, help='additional similarity metric')
    parser.add_argument('third_matrix', type=str, help='another additional similarity metric')
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

    pcw2v = get_df(args.primary_matrix)
    jac = get_df(args.second_matrix)
    combined = combine_and_weight(pcw2v, jac)


    source_idxs, comp_idxs, thresh_values = get_indices_and_values(combined, args.thresh)

    thresh_source_sents = pd.DataFrame(extract_from_df(source_df, source_idxs, 0))
    thresh_s_og_idxs = pd.DataFrame(extract_from_df(source_df, source_idxs, 1))
    thresh_s_idxs = pd.DataFrame(source_idxs)
    thresh_source = pd.concat([thresh_source_sents, thresh_s_og_idxs, thresh_s_idxs], axis=1, ignore_index=True) 
    
    thresh_comp_sents = pd.DataFrame(extract_from_df(comp_df, comp_idxs, 0))
    thresh_c_og_idxs = pd.DataFrame(extract_from_df(comp_df, comp_idxs, 1))
    thresh_c_idxs = pd.DataFrame(comp_idxs)
    thresh_comp = pd.concat([thresh_comp_sents, thresh_c_og_idxs, thresh_c_idxs], axis=1, ignore_index=True)

    source_sents, comp_sents, og_s_idxs, og_c_idxs, s_idxs, c_idxs, values = filter_sentence_length(thresh_source, thresh_comp, thresh_values)

    matrix3 = get_df(args.third_matrix)
    values3 = values_at_indices(matrix3.values, s_idxs, c_idxs)

    og_s_sents = extract_from_df(og_source_df, og_s_idxs, 0)
    og_c_sents = extract_from_df(og_comp_df, og_c_idxs, 0)

    sents_fp = args.out_file + ".sents.clean.thresh"
    idxs_fp = args.out_file + ".idxs.og.thresh"
    og_sents_fp = args.out_file + ".sents.og.thresh"
    
    write_csv(sents_fp, source_sents.values, comp_sents.values, values, values3)
    write_csv(idxs_fp, og_s_idxs.values, og_c_idxs.values, values, values3)
    write_csv(og_sents_fp, og_s_sents, og_c_sents, values, values3)

if __name__== "__main__":
    main()
