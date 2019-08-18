# Import files
import argparse
import gensim
from gensim.models import Word2Vec
from sklearn.decomposition import TruncatedSVD
import numpy as np
import pandas as pd
from datetime import datetime
import csv
from create_w2v import EpochLogger 

def logging(x, logfile):
	tex="logged: "+x+" on "+str(datetime.today().ctime())
	with open(logfile,'a') as f:
		f.write(tex)
		f.write("\n")

class MySentences(object):
    def __init__(self, filename):
        self.filename = filename
 
    def __iter__(self):
        for line in open(self.filename):
            yield line.lower().split()

def create_sentence_vectors(vecs, input_file):
    """
    given a list of lists, with the inner lists representing sentences, split into words
    return vector representations of each sentence (by averaging all the words)
    """
    ret = []
    for sentence in MySentences(input_file):
        ret.append(np.mean(vecs[sentence], axis=0))
    return ret    

def compute_pc(X,npc=1):
    """
    From: https://github.com/PrincetonML/SIF/blob/master/src/SIF_embedding.py
    Compute the principal components. DO NOT MAKE THE DATA ZERO MEAN!
    :param X: X[i] is a data point
    :param npc: number of principal components to remove
    :return: component_[i] is the i-th pc
    """
    svd = TruncatedSVD(n_components=npc, n_iter=7, random_state=0)
    svd.fit(X)
    return svd.components_

def main():
    parser = argparse.ArgumentParser(description='parse arguments')
    parser.add_argument('input_file', type=str, help='source file')
    parser.add_argument('model_file', type=str, help='file with the model to load')
    parser.add_argument('out_file', type=str, help='output file')
    args = parser.parse_args()
    # logfile = "log." + args.out_file

    model = gensim.models.Word2Vec.load(args.model_file)
    vecs = model.wv

    sentence_vectors = create_sentence_vectors(vecs, args.input_file)
    components = compute_pc(sentence_vectors)
    np.savetxt(args.out_file, components)

if __name__== "__main__":
  main()