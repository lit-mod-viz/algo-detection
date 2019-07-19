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
                counts.update(line.strip().split(' '))
    except (IOError, OSError):
        print("Error opening / processing file")

def remove_words(path, remove_list):
    """
    """
    try:
        with open(path) as file_handler:
            for line in read_file(file_handler):
                # TODO: write line out to a different file with a tweak
                pass
    except (IOError, OSError):
        print("Error opening / processing file")

def write_to_remove(remove_file, stopwords, hapaxes):
    with open(remove_file, 'w') as fh:
        for word in stopwords:
            fh.write(word)
            fh.write("\n")
        for hapax in hapaxes:
            fh.write(hapax)
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

    args = parser.parse_args()
    counts = Counter()
    build_counter(args.input_file, counts)
    print(len(counts))

    stopwords = get_stopwords()
    hapaxes = get_hapaxes(counts)

    write_to_remove(args.remove_file, stopwords, hapaxes)
    
if __name__== "__main__":
  main()
