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
            write_file(obj, directory + filename, ".lemmatized")

def lemmatize_csv(input_file, output_file, nlp):
    """
    """
    try:
        with open(path) as read_fh, open(output_path, 'w') as write_fh:
            nlp = spacy.load('en', disable=['parser','ner'])

            reader = csv.reader(read_fh, delimiter=',')
            writer = csv.writer(write_fh)

            for line in reader:
                # write line out to a different file with junky words removed
                index = line[1]
                doc = nlp(line[0].strip())
                cleaned = " ".join([token.lemma_ for token in doc]))
                row = [cleaned, index]
                writer.writerow(row)

    except (IOError, OSError):
        print("Error opening / processing file")