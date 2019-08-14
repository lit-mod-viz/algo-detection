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

def remove_blanks(path, output_path):
    """
    """
    try:
        with open(path) as read_fh, open(output_path, 'w') as write_fh:
            for line in read_file(read_fh):
                # write line out to a different file with blanks removed
                if line:
                    cleaned = " ".join([word for word in line.split() if word != ''])
                    write_fh.write(cleaned)
                    write_fh.write('\n')
                else:
                    print("BLANKS")

    except (IOError, OSError):
        print("Error opening / processing file")

def remove_blanks_csv(path, output_path):
    """
    """
    try:
        with open(path) as read_fh, open(output_path, 'w') as write_fh:
            reader = csv.reader(read_fh, delimiter=',')
            writer = csv.writer(write_fh)
            
            for line in reader:
                # write line out to a different file with blanks removed
                index = line[1]
                if line[0] != '':
                    cleaned = " ".join([word for word in line[0].split() if word != ''])
                    row = [cleaned, index]
                    writer.writerow(row)
    except (IOError, OSError):
        print("Error opening / processing file")

def main():
    parser = argparse.ArgumentParser(description='parse arguments')
    parser.add_argument('input_file', type=str, help='file to read')
    parser.add_argument('extension', type=str, help='file extension to append to input file for naming output')

    args = parser.parse_args()
    altered_file = args.input_file + args.extension

    remove_blanks(args.input_file, altered_file)
    # remove_blanks_csv(args.input_file, altered_file)


if __name__== "__main__":
  main()
