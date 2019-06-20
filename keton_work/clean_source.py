import re

def fill_sentences(text):
    l = re.split(r'([\d]+[.])', text)
    nums = re.findall(r'([\d]+[.])', text)
    diff = [item for item in l if item not in nums]
    nested = [sent.split('\n\n') for sent in diff]
    cleaned = []
    for l in nested:
        cleaned.append([item.rstrip().lstrip() for item in l])
    
if __name__ = if __name__ == "__main__":
    pass