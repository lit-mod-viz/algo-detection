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

def logging(x):
	tex="logged: "+x+" on "+str(datetime.today().ctime())
	with open('similarity-logger.txt','a') as f:
		f.write(tex)
		f.write("\n")

def process_file_as_list(filename, model):  
    with open(filename,'r') as f:
        lines = f.read()
    tokens =  lines.split('\n')
    corpus = [element.split(" ") for element in tokens]
    pared_corpus = []
    for line in corpus:
        if line != ['']: #remove any extra blank words in the list
            #TODO: Get stats on how much is not in the model vocab and check if google stuff is lemmatized
            pared_corpus.append([elem for elem in line if elem != '' and elem in model.vocab])
    junk = [item for item in corpus if item not in pared_corpus]
    return pared_corpus, junk

def sentence_similarities(source_list, compare_list, model):
    # Calculate the similarity between every sentence in the source and every sentence in the test
    # TODO: Convert to lazy writing. Similarity might not fit into memory with full target
    similarity = []
    for test_sentence in compare_list: #iterate over every sentence in the test corpus
        similarities = []
        for source_sentence in source_list: #for every sentence in the test, iterate over every sentence in the source
            if source_sentence and test_sentence:
                similarities.append((test_sentence, source_sentence, model.n_similarity(source_sentence,test_sentence)))
        # Out of all similarities for each sentence in the test to every sentence in the source, get the maximum one
        similarity.append(similarities)
    return similarity

def write_out(out_file, output):
    with open(out_file, 'w') as out:
        writer = csv.writer(out)
        writer.writerows(output)

def write_junk(outfile, junk):
    with open(outfile, 'w') as f:
        f.write(junk)

def main():
    parser = argparse.ArgumentParser(description='parse arguments')
    parser.add_argument('source_file', type=str, help='source file')
    parser.add_argument('compare_file', type=str, help='file being compared to source')
    parser.add_argument('out_file', type=str, help='output file')
    args = parser.parse_args()
    
    model = gensim.models.KeyedVectors.load_word2vec_format('/home/ketonkakkar/GoogleNews-vectors-negative300.bin', binary='True')
    # logging("loaded model")

    source_list, source_junk = process_file_as_list(args.source_file, model)
    # logging("made source list")

    compare_list, compare_junk = process_file_as_list(args.compare_file, model)
    # logging("made test list")

    similarities_list = sentence_similarities(source_list, compare_list, model)
    # logging("finished calculating similarities")

    # write_out(args.out_file, similarities_list)
    # logging("wrote to file")

   # write_junk("junk-source.txt", source_junk)
   #  write_junk("junk-compare.txt", compare_junk)

if __name__== "__main__":
  main()
