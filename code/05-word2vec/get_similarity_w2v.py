# Import files
import argparse
import gensim
from gensim.models import Word2Vec
from gensim import corpora
import numpy as np
import pandas as pd
from sklearn.manifold import TSNE
from datetime import datetime
import matplotlib.pyplot as plt
import csv
from create_w2v import EpochLogger 

def logging(x):
	tex="logged: "+x+" on "+str(datetime.today().ctime())
	with open('similarity-logger.txt','a') as f:
		f.write(tex)
		f.write("\n")

class MySentences(object):
    def __init__(self, filename):
        self.filename = filename
 
    def __iter__(self):
        for line in open(self.filename):
            yield line.lower().split()

def create_sentence_vectors(model, compare_file):
    """
    given a list of lists, with the inner lists representing sentences, split into words
    return vector representations of each sentence (by averaging all the words)
    """
    ret = []
    for sentence in MySentences(compare_file):
        if not sentence:
            print("BLANK LIST")
        if '' in sentence:
            print("CONTAINS EMPTY STRING")
        ret.append(np.mean(model[sentence], axis=0))
    return ret

def smart_similarities(vecs, source_file, compare_vectors):
    for sentence in MySentences(source_file):
        sentence_vector = np.mean(vecs[sentence], axis=0)
        yield vecs.cosine_similarities(sentence_vector, compare_vectors)
    

def write_smart_similarities(out_file, model, source_file, compare_vectors):
    with open(out_file, 'w') as out:
        writer = csv.writer(out)
        writer.writerows(smart_similarities(model, source_file, compare_vectors))

def write_junk(outfile, junk):
    with open(outfile, 'w') as f:
        f.write(junk)

def main():
    parser = argparse.ArgumentParser(description='parse arguments')
    parser.add_argument('source_file', type=str, help='source file')
    parser.add_argument('compare_file', type=str, help='file being compared to source')
    parser.add_argument('model_file', type=str, help='file with the model to load')
    parser.add_argument('out_file', type=str, help='output file')
    args = parser.parse_args()
    
    # NOTE: Word2Vec.load is the function to call for our model
    model = gensim.models.Word2Vec.load(args.model_file)
    # model = gensim.models.KeyedVectors.load_word2vec_format("GoogleNews-vectors-negative300.bin", binary=True)
    vecs = model.wv
    compare_vectors = create_sentence_vectors(model, args.compare_file)
    write_smart_similarities(args.out_file, vecs, args.source_file, compare_vectors)

if __name__== "__main__":
  main()
