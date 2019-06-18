import spacy

def segment(text, nlp):
    ret = []
    doc = nlp(text)
    for sentence in doc.sents:
        ret.append(sentence.text)
    return ret

def main():
    nlp = spacy.load('en')
    with open("output/argosy-1917.txt.clean", 'r') as fp:
        text = fp.read()
        obj = segment(text, nlp)
    with open ("output/argosy-1917.txt.clean.newsegmented", 'w') as f:
        f.writelines(obj)

if __name__== "__main__":
  main()
