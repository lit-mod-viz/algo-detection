# Import files
import argparse
import matplotlib.pyplot as plt
import csv
import numpy as np
import pandas as pd
import gensim
from gensim import corpora
from gensim import models
from gensim import similarities
from gensim.models import Word2Vec
from sklearn.manifold import TSNE
from datetime import datetime
from gensim.parsing.preprocessing import remove_stopwords
from gensim.test.utils import get_tmpfile

def logging(x):
	tex="logged: "+x+" on "+str(datetime.today().ctime())
	with open('similarity-logger.txt','a') as f:
		f.write(tex)
		f.write("\n")

def write_out(out_file, output):
    with open(out_file, 'w') as out:
        writer = csv.writer(out)
        writer.writerows(output)

def process_file_as_list(filename):  
    with open(filename,'r') as f:
        lines = f.read()
    tokens =  lines.split('\n')
    tokens = [remove_stopwords(token) for token in tokens]
    corpus = [element.split(" ") for element in tokens]
    # TODO: remove stop words
    pared_corpus = []
    for line in corpus:
        if line != ['']: #remove any extra blank words in the list
            pared_corpus.append([elem for elem in line if elem != ''])
    # TODO: also remove words that appear only once
    return pared_corpus

def make_corpus_and_dict(sentence_list):
    dictionary = corpora.Dictionary(sentence_list)
    corpus = [dictionary.doc2bow(sentence) for sentence in sentence_list]    
    tfidf_model = models.TfidfModel(corpus)

    return dictionary, corpus, tfidf_model

def make_index(training_dict, lsi, tfidf_model, sentence_list):
    index_tmpfile = get_tmpfile("index")
    pass

def main():
    parser = argparse.ArgumentParser(description='parse arguments')
    parser.add_argument('source_file', type=str, help='source file')
    parser.add_argument('compare_file', type=str, help='file being compared to source')
    # parser.add_argument('training_file')
    parser.add_argument('out_file', type=str, help='output file')
    args = parser.parse_args()
    source_list = process_file_as_list(args.source_file)
    compare_list = process_file_as_list(args.compare_file)
    # training_list = process_file_as_list(args.training_file)

    # training_dict, training_corpus, training_tfidf = make_corpus_and_dict(training_list)
    new_dict, new_corpus, new_tfidf = make_corpus_and_dict(compare_list)
    input_corpus = [new_dict.doc2bow(sentence) for sentence in compare_list]    

    lsi = models.LsiModel(new_tfidf[input_corpus], id2word=new_dict, num_topics=300)
    # lsi.add_documents(new_tfidf[new_corpus])
    index = similarities.MatrixSimilarity(lsi[new_tfidf[input_corpus]])

    # lsi.add_documents()
    # index = make_index(dictionary, lsi, tfidf_model, compare_list)
    # print(index)

    sims = []
    for i, sentence in enumerate(source_list):
        vec_bow = new_dict.doc2bow(sentence)
        tfidf_bow = new_tfidf[vec_bow]
        vec_lsi = lsi[tfidf_bow]
        neat = sorted(enumerate(index[vec_lsi]), key=lambda item: -item[1])
        #TODO: If an item hits higher than 90% similarity print the two sentences and doc number to a file 
        sims.append(neat[0:9])

    write_out(args.out_file, sims)

if __name__== "__main__":
  main()
