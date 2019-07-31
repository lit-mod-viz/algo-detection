import argparse
import csv

def read_file(file_object):
    """
    Uses a generator to read a large file lazily
    """
    while True:
        data = file_object.readline()
        if not data:
            break
        yield data

def number_lines(path, output_path):
    """
    """
    try:
        with open(path) as read_fh, open(output_path, 'w') as write_fh:
            writer = csv.writer(write_fh)
            for i, line in enumerate(read_file(read_fh)):
                row = [line, i]
                writer.writerow(row)

    except (IOError, OSError):
        print("Error opening / processing file")

def main():
    parser = argparse.ArgumentParser(description='parse arguments')
    parser.add_argument('input_file', type=str, help='file to read')
    parser.add_argument('extension', type=str, help='file extension to append to input file for naming output')

    args = parser.parse_args()
    altered_file = args.input_file + args.extension
    
    number_lines(args.input_file, altered_file)

if __name__== "__main__":
  main()
