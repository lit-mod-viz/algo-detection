import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords

import argparse

def main():
    stops = set(stopwords.words("english"))
    parser = argparse.ArgumentParser(description='parse arguments')
    parser.add_argument('filename', metavar='N', type=str, nargs='+',
                        help='input filename without extension')
    args = parser.parse_args()

    with open(args.filename + ".txt", 'r') as f:
        text = f.read()

    sentences = text.split("\n")
    words = [element.split(" ") for element in sentences]
    stopped = [word for word in words if word not in stops]

    with open(args.filename + ".stop", 'w') as fp:
        for line in stopped:
            fp.write(" ".join(line))

if __name__ == "__main__":
    main()