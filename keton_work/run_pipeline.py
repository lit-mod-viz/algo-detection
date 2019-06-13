import os
import argparse
from clean import do_process
from no_solos import remove_solos
def clean_all_files(directory):
    for filename in os.listdir(directory):
        print(filename)
        do_process(directory + filename)

def segment_all_files(directory, extension):
    bad_chars = [" ", "(", ")"]
    for filename in os.listdir(directory):
        if filename.endswith(extension):
            for bad_char in bad_chars:
                if bad_char in filename:
                    filename = filename.replace(bad_char, "\{0}".format(bad_char))
            filepath = directory + filename
            os.system("python3 -m syntok.segmenter " + filepath + " > " + "output/" + filename + ".segmented")

def weed_solos_all_files(directory, extension):
    bad_chars = [" ", "(", ")"]
    for filename in os.listdir(directory):
        if filename.endswith(extension):
            remove_solos(directory + filename)

def main():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('directory', metavar='N', type=str, nargs='+',
                        help='path to directory')
    args = parser.parse_args()
    clean_all_files(args.directory[0])
    segment_all_files("output/", ".clean")
    weed_solos_all_files("output/", ".segmented")

if __name__== "__main__":
  main()
