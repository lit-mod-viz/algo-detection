import argparse
import pandas as pd
from top_sentence_indices import get_indices_and_values, get_df, write_csv, extract_from_df


def main():
    parser = argparse.ArgumentParser(description='parse arguments')
    parser.add_argument('matrix_file', type=str, help='matrix file')
    parser.add_argument('source_file', type=str, help='file with source sentences used to generate matrix')
    parser.add_argument('comp_file', type=str, help='file with compare sentences used to generate matrix')
    parser.add_argument('out_file', type=str, help='file to write out to')      
    parser.add_argument('index_file', type=str, help='if og = true: read; else: write')    

    args = parser.parse_args()

    source_df = get_df(args.source_file)
    comp_df = get_df(args.comp_file)
        
    info_df = pd.read_csv(args.index_file,sep=',')
    
    source_idxs = info_df["Source"]
    comp_idxs = info_df["Compare"]
    values = info_df["Value"]

    source_sents = extract_from_df(source_df, source_idxs, 0)
    comp_sents = extract_from_df(comp_df, source_idxs, 0)

    if not args.og:
        write_csv(args.og_indices_file, og_s_idxs, og_c_idxs, values)

    write_csv(args.out_file, source_sents, comp_sents, values)

if __name__== "__main__":
    main()