import string
import re

def read_file_to_list(filepath):
    ret = []    
    for line in open(filepath, 'r'):
        ret.append(line)
    return ret

def remove_solos(text):
    """
    returns the text at the given file path in the form of a list without single word sentences
    also returns a separate list with the discarded single word sentences
    """
    ret = []
    discard = []
    for line in text:
        if len(line.split()) > 1:
            ret.append(line)
        else:
            discard.append(line)
    return ret, discard

def remove_hyphens(text):
    """
    removes words that are hyphenated as a result of having been split accross a line-break in OG text
    returns new text as a list
    """
    ret = [re.sub(r'[-–—¬]\s+', '', sentence) for sentence in text]
    return ret

def make_lower(text):
    ret = [sentence.lower() for sentence in text]
    return ret

def remove_punctuation(text):
    ret = [re.sub(r'[^a-zA-Z\d\s]', '', sentence) for sentence in text]
    # ret = [' '.join(sentence.split()) for sentence in text]
    # ret = [sentence.translate(str.maketrans('', '', string.punctuation)) for sentence in text]
    return ret

def write_file(text, filepath, extension):
    with open (filepath + extension, 'w') as f:
        f.writelines(text)

def post_seg(directory, filename):
    obj = read_file_to_list(directory + filename)
    # obj, discard = remove_solos(obj)
    # obj = remove_hyphens(obj)
    obj = make_lower(obj)
    obj = remove_punctuation(obj)
    write_file(obj, directory + filename, ".stripped")
    # write_file(discard, "output/" + filename, ".discardedsolos")

def main():
    filename = "short-story-pg.sentences.txt.clean.segmented"
    post_seg("../processed-corpus/test-output/", filename)
   

if __name__== "__main__":
  main()
