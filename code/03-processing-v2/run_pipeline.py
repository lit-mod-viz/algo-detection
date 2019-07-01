import os
import argparse
from clean import do_process
from no_solos import post_seg
from lemmatizer import lemmatize_all_files

def clean_all_files(input_directory, output_directory):
    for i, filename in enumerate(os.listdir(input_directory)):
        do_process(input_directory, output_directory, filename, i)

def segment_all_files(directory, extension):
    for filename in os.listdir(directory):
        if filename.endswith(extension):
            filepath = directory + filename
            os.system("python3 -m syntok.segmenter " + filepath + " > " + directory + filename + ".segmented")

def post_seg_all_files(directory, extension):
    for filename in os.listdir(directory):
        if filename.endswith(extension):
            post_seg(directory, filename)

def main():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('input_directory', metavar='N', type=str, nargs='+',
                        help='path to input directory')
    parser.add_argument('output_directory', metavar='N', type=str, nargs='+', help='path to output directory')
    args = parser.parse_args()
    clean_all_files(args.input_directory[0], args.output_directory[0])
    segment_all_files(args.output_directory[0], ".clean")
    post_seg_all_files(args.output_directory[0], ".segmented")
    lemmatize_all_files(args.output_directory[0], ".stripped")

if __name__== "__main__":
  main()
