# -*- coding: utf-8 -*-
import gensim
from gensim.models import TfidfModel
from gensim.models.callbacks import CallbackAny2Vec
from gensim import corpora
from corpora import Dictionary
import os
import cython
import numpy as np
import pandas as pd
from datetime import datetime
import smart_open
import multiprocessing
import argparse

# Read all files and create training corpus

def logging(x):
	tex="logged: "+x+" on "+str(datetime.today().ctime())
	with open('TFIDF-model-logger.txt','a') as f:
		f.write(tex)
		f.write("\n")

class MySentences(object):
    def __init__(self, filename):
        self.filename = filename
 
    def __iter__(self):
        for line in open(self.filename):
            yield line.split()

class EpochLogger(CallbackAny2Vec):
    def __init__(self):
        self.epoch = 1

    def on_epoch_begin(self, model):
        logging("Epoch #{} start".format(self.epoch))

    def on_epoch_end(self, model):
        logging("Epoch #{} end".format(self.epoch))
        self.epoch += 1

def create_dictionary(training_corpus):
    dct = Dictionary(training_corpus)
    return dct

def create_model(dct, training_corpus):
    # Train the tfidf model on the corpus
    corpus = [dct.doc2bow(line) for line in training_corpus]
    logging('Made bag of words')
    model = TfidfModel(corpus)
    return model 

def main():
    gensim.models.word2vec.FAST_VERSION = 1

    parser = argparse.ArgumentParser(description='parse arguments')
    parser.add_argument('input_file', type=str, help='file to read')
    parser.add_argument('output_file', type=str, help='file to write model out to')

    args = parser.parse_args()
    logging('Begin loading sentences')
    training_corpus = list(MySentences(args.input_file))
    logging('Finished loading sentences')

    logging('begin making dictionary ')
    dct = create_dictionary(training_corpus)
    logging('dictionary made')
    dct.save(args.output_file + ".dict")
    logging('dictionary saved')

    """ logging('Training model begins')
    model = create_model(dct, training_corpus)
    logging('Training ended')
    model.save(args.output_file)
    logging('Model saved') """

if __name__== "__main__":
  main()



# Train the word2vec model on the corpus

