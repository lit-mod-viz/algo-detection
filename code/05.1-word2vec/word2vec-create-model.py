# -*- coding: utf-8 -*-
import gensim
from gensim.models import Word2Vec
from gensim.models.callbacks import CallbackAny2Vec
from gensim import corpora
import os
import cython
import numpy as np
import pandas as pd
import glob
from datetime import datetime

gensim.models.word2vec.FAST_VERSION = 1

# Read all files and create training corpus

def logging(x):
	tex="logged: "+x+" on "+str(datetime.today().ctime())
	with open('create-model-logger.txt','a') as f:
		f.write(tex)
		f.write("\n")

class MySentences(object):
    def __init__(self, dirname):
        self.dirname = dirname
 
    def __iter__(self):
        for subdir, dirs, files in os.walk(self.dirname):
            for fname in files:
                if fname != '.DS_Store':
                    for line in open(os.path.join(subdir, fname)):
                        yield line.split()

class EpochLogger(CallbackAny2Vec):
    def __init__(self):
        self.epoch = 1

    def on_epoch_begin(self, model):
        logging("Epoch #{} start".format(self.epoch))

    def on_epoch_end(self, model):
        logging("Epoch #{} end".format(self.epoch))
        self.epoch += 1


logging('creating Training corpus')
training_corpus = MySentences('../pre-processing/')
logging('created training corpus')


# Train the word2vec model on the corpus

epoch_logger = EpochLogger()
logging('Training model begins')
model = Word2Vec(training_corpus, iter=50, size=50, window=3, min_count=1, workers=8, sg=1, callbacks=[epoch_logger])
logging('Training ended')

model.save('word2vec_model.model')
logging('Model saved')