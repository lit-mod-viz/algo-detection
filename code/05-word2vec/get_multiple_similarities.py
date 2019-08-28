# Import files
import argparse
import gensim
from gensim.models import Word2Vec
from gensim.models import TfidfModel
from gensim import corpora
from gensim.corpora import Dictionary
import numpy as np
import pandas as pd
from sklearn.manifold import TSNE
from datetime import datetime
import matplotlib.pyplot as plt
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

def create_sentence_vectors(model, compare_file, pc):
    """
    given a list of lists, with the inner lists representing sentences, split into words
    return vector representations of each sentence (by averaging all the words)
    """
    pc_ret = []
    for sentence in MySentences(compare_file):
        pc_ret.append(remove_pc(np.mean(model[set(sentence)], axis=0), pc))
    return pc_ret

def two_similarities(vecs, source_file, comp_vecs_sans_pc, pc):
    for sentence in MySentences(source_file):
        source_vector = np.mean(vecs[set(sentence)], axis=0)
        souce_vector_sans_pc = remove_pc(source_vector, pc)
        pc_sims = vecs.cosine_similarities(souce_vector_sans_pc, comp_vecs_sans_pc)
        yield pc_sims

def write_two_similarities(pc_fp, model, source_file, comp_vecs_sans_pc, pc):
    with open(pc_fp, 'w') as pc_fh:
        pc_writer = csv.writer(pc_fh)
        for pc_sims in two_similarities(model, source_file, comp_vecs_sans_pc, pc):
            pc_writer.writerow(pc_sims)

def get_two_similarities(model_file, component_file, out_file, source_file, compare_file, logfile):
    # NOTE: Word2Vec.load is the function to call for our model. 
    # Use the line below for the google model
    # model = gensim.models.KeyedVectors.load_word2vec_format("GoogleNews-vectors-negative300.bin", binary=True)

    logging("begin loading w2v model", logfile)
    model = gensim.models.Word2Vec.load(model_file)
    logging("end loading w2v model", logfile)
    vecs = model.wv
    pc = np.loadtxt(component_file)
    logging("begin making compare array with pc removed", logfile)
    comp_vecs_sans_pc = np.array(create_sentence_vectors(vecs, compare_file, pc))
    logging("end making compare array", logfile)
    logging("begin comparisons", logfile)
    write_two_similarities("pc_w2v_" + out_file, vecs, source_file, comp_vecs_sans_pc, pc)
    logging("end comparisons", logfile)

def remove_pc(X, pc, npc=1):
    """
    Adapted from: https://github.com/PrincetonML/SIF/blob/master/src/SIF_embedding.py
    Remove the projection on the principal components
    :param X: X[i,:] is a data point
    :param npc: number of principal components to remove
    :return: XX[i, :] is the data point after removing its projection
    """
    if npc==1:
        XX = X - X.dot(pc.transpose()) * pc
    else:
        XX = X - X.dot(pc.transpose()).dot(pc)
    return XX

def pc_w2v_similarities(pc_file, ):
    pc = np.loadtxt(pc_file)

def SIF_weighting(a, word, vecs):
    """
    # where a is a parameter often set to .001
    """
    weight = a/(a+vecs.vocab[word].count)
    return weight * vecs[word]

def jaccard(S,C):
    intersection = S.intersection(C)
    union = S.union(C)
    return len(intersection)/len(union)

def compare_jaccard(source_file, compare_file):
    for source in MySentences(source_file):
        row = []
        for compare in MySentences(compare_file):
            row.append(jaccard(set(source), set(compare)))
        yield row

def write_jaccard(out_file, source_file, compare_file):
    with open(out_file, 'w') as out:
        writer = csv.writer(out)
        writer.writerows(compare_jaccard(source_file, compare_file))

def get_jaccard_similarities(out_file, source_file, compare_file):
    write_jaccard(out_file, source_file, compare_file)

""" def get_tfidf_vector_similarities(model_file, dict_file, source_file, compare_file):
    dct = Dictionary.load(dict_file)
    model = TfidfModel.load(model_file)
    for line in list(MySentences(source_file))]
        source = dct.doc2bow(line) 
        for line in list(MySentences(compare_file)):
            comp = dct.doc2bow(line)

            # these should be a list of tuples, with the vector being the second index in the tuple
            model[source] 
            model[comp]

            # get similarities. Maybe there's a built-in way to do this with Gensim.
            # different length sentences. Ask Dennis """


def main():
    parser = argparse.ArgumentParser(description='parse arguments')
    parser.add_argument('source_file', type=str, help='source file')
    parser.add_argument('compare_file', type=str, help='file being compared to source')
    parser.add_argument('out_file', type=str, help='output file')

    parser.add_argument('model_file', type=str, help='file with the model to load')
    parser.add_argument('component_file', type=str, help='file with the principal component that you wish to remove')

    args = parser.parse_args()
    logfile = "log." + args.out_file

    w2v = True
    jaccard = True
    if w2v:
        logging("begin w2v - pc", logfile)
        get_two_similarities(args.model_file, args.component_file, args.out_file, args.source_file, args.compare_file, logfile)
        logging("end w2v - pc", logfile)

    if jaccard:
        logging("begin jaccard", logfile)
        get_jaccard_similarities("jac_"+args.out_file, args.source_file, args.compare_file)
        logging("end jaccard", logfile)

if __name__== "__main__":
  main()
