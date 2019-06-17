import spacy
import re
import os
from no_solos import read_file_to_list, write_file

def lemmatize(text, nlp):
    ret = []
    for sentence in text:
        doc = nlp(sentence)
        ret.append(" ".join([token.lemma_ for token in doc]))
    return ret

def lemmatize_all_files(directory, extension):
    nlp = spacy.load('en', disable=['parser','ner'])
    for filename in os.listdir(directory):
        if filename.endswith(extension):
            obj = read_file_to_list(directory + filename)
            obj = lemmatize(obj, nlp)
            write_file(obj, "output/" + filename, ".lemmatized")
