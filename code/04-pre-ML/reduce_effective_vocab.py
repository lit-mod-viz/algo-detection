import argparse
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

def process_file(path, count_dict):

    """"""
    try:
        with open(path) as file_handler:
            for line in read_file(file_handler):
                # process line
                count_dict.update(line.strip().split(' '))
    except (IOError, OSError):
        print("Error opening / processing file")
 
def main():
    parser = argparse.ArgumentParser(description='parse arguments')
    parser.add_argument('input_file', type=str, help='source file')
    args = parser.parse_args()
    count_dict = Counter()
    process_file(args.input_file, count_dict)
    print(count_dict)
    print(len(count_dict))

if __name__== "__main__":
  main()