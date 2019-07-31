# Import files
import gensim
from gensim.models import Doc2Vec
from gensim.models.word2vec import LineSentence
from gensim.test.utils import datapath
from gensim import corpora

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import multiprocessing
import argparse
import smart_open
from sklearn.manifold import TSNE


class MySentences(object):
    def __init__(self, filename):
        self.filename = filename
 
    def __iter__(self):
        with smart_open.smart_open(self.filename) as f:
            for i, line in enumerate(f):
                yield gensim.models.doc2vec.TaggedDocument(line, [i])

def create_model(input_file, output_file):
    training_corpus = list(MySentences(input_file))
    
    # Train the word2vec model on the corpus
    cores = multiprocessing.cpu_count()

    model = Doc2Vec(window=3, workers=1)
    model.build_vocab(training_corpus)
    model.train(training_corpus, total_examples=len(training_corpus), epochs=10)
    model.save(output_file)

def main():
    parser = argparse.ArgumentParser(description='parse arguments')
    parser.add_argument('input_file', type=str, help='file to read')
    parser.add_argument('output_file', type=str, help='file to write model out to')

    args = parser.parse_args()
    create_model(args.input_file, args.output_file)

if __name__== "__main__":
  main()
