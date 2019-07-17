import nltk
from nltk.corpus import stopwords

import argparse

def main():
    stops = stopwords.words("english")
    parser = argparse.ArgumentParser(description='parse arguments')
    parser.add_argument('filename', metavar='N', type=str, nargs='+',
                        help='input filename without extension')
    args = parser.parse_args()

    with open(args.filename[0] + ".txt", 'r') as f:
        text = f.read()
    print(type(stops))
    sentences = text.split("\n")
    words = [element.split(" ") for element in sentences]
    stopped = [word for word in words if word not in stops]

    with open(args.filename[0] + ".stop", 'w') as fp:
        for line in stopped:
            fp.write(" ".join(line))
            fp.write('\n')
if __name__ == "__main__":
    main()
