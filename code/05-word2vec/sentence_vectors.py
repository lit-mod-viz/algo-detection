import gensim
import argparse
import numpy as np
import pickle
from datetime import datetime

def logging(x):
	tex="logged: "+x+" on "+str(datetime.today().ctime())
	with open('sentence-vector-logger.txt','a') as f:
		f.write(tex)
		f.write("\n")

def load_text(filepath):
    with open(filepath, 'r') as fp:
        text = fp.read()
    logging("loaded text")
    return text

def get_sentence_vectors(text):
    retlist = []
    model = gensim.models.KeyedVectors.load_word2vec_format('/home/ketonkakkar/GoogleNews-vectors-negative300.bin', binary='True')
    logging("loaded model!")
    for sentence in text:
        retlist.append(get_mean_vector(model, sentence))
    return retlist

def get_mean_vector(model, words):
    # remove out-of-vocabulary words
    words = [word for word in words if word in model.vocab]
    if len(words) >= 1:
        return np.mean(model[words], axis=0)
    else:
        return []

def write_to_file(object, out_file):
    with open(out_file, 'wb') as out:
        pickle.dump(object, out)

def main():
    parser = argparse.ArgumentParser(description='parse arguments')
    parser.add_argument('input_file', type=str, help='input file')
    parser.add_argument('out_file', type=str, help='output file')
    args = parser.parse_args()
    text = load_text(args.input_file)
    sentence_vectors = get_sentence_vectors(text)
    logging("created vectors of all sentences")
    write_to_file(sentence_vectors, args.out_file)

if __name__== "__main__":
    main()

