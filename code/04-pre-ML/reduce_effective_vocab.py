import argparse
import nltk
from nltk.corpus import stopwords
from collections import Counter

def read_file(file_object):
    """
    Uses a generator to read a large file lazily
    """
    while True:
        data = file_object.readline()
        if not data:
            break
        yield data

def build_counter(path, counts):
    """
    """
    try:
        with open(path) as file_handler:
            for line in read_file(file_handler):
                # process line
                counts.update(line.lower().strip().split(' '))
    except (IOError, OSError):
        print("Error opening / processing file")

def load_remove_set(path, rset):
    """
    """
    try:
        with open(path) as file_handler:
            for line in read_file(file_handler):
                rset.add(line.strip())
    except (IOError, OSError):
        print("Error opening / processing file")

def remove_words(path, output_path, remove_list):
    """
    """
    try:
        with open(path) as read_fh, open(output_path, 'w') as write_fh:
            for line in read_file(read_fh):
                # write line out to a different file with junky words removed
                cleaned = " ".join([word for word in line.split() if word not in remove_list])
                write_fh.write(cleaned)
                write_fh.write('\n')

    except (IOError, OSError):
        print("Error opening / processing file")

def write_to_remove(remove_file, remove_list):
    with open(remove_file, 'w') as fh:
        for word in remove_list:
            fh.write(word)
            fh.write("\n")

def get_stopwords():
    temp = stopwords.words("english")
    stops = [s.replace("'", "") for s in temp]
    return stops

def get_hapaxes(counts):
    hapaxes = [word for word in counts if counts[word] == 1]
    return hapaxes

def main():
    parser = argparse.ArgumentParser(description='parse arguments')
    parser.add_argument('input_file', type=str, help='file to read')
    parser.add_argument('remove_file', type=str, help='file for writing words we want to remove')
    parser.add_argument('extension', type=str, help='file extension to append to input file for naming output')

    args = parser.parse_args()
    altered_file = args.input_file + args.extension
    counts = Counter()
    rset = set()
    build_counter(args.input_file, counts)
    print(len(counts))
    stopwords = get_stopwords()
    hapaxes = get_hapaxes(counts)
    remove_list = stopwords + hapaxes
    rset = set(remove_list)
    write_to_remove(args.remove_file, remove_list)
    # load_remove_set(args.remove_file, rset)
    remove_words(args.input_file, altered_file, rset)

if __name__== "__main__":
  main()
