import os
import argparse
from clean import do_process
from no_solos import post_seg
from lemmatizer import lemmatize_all_files

def clean_all_files(directory):
    for i, filename in enumerate(os.listdir(directory)):
        do_process(directory, filename, i)

def segment_all_files(directory, extension):
    for filename in os.listdir(directory):
        if filename.endswith(extension):
            filepath = directory + filename
            os.system("python3 -m syntok.segmenter " + filepath + " > " + "../processed-corpus/test-output/" + filename + ".segmented")

def post_seg_all_files(directory, extension):
    for filename in os.listdir(directory):
        if filename.endswith(extension):
            post_seg(directory, filename)

def main():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('directory', metavar='N', type=str, nargs='+',
                        help='path to directory')
    args = parser.parse_args()
    clean_all_files(args.directory[0])
    segment_all_files("../processed-corpus/test-output/", ".clean")
    post_seg_all_files("../processed-corpus/test-output/", ".segmented")
    lemmatize_all_files("../processed-corpus/test-output/", ".stripped")

if __name__== "__main__":
  main()
