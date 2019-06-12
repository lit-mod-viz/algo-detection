import re

def read_and_strip(filename):
    """ 
    input: path to a file
    output: a string with the contents of the file stripped of newlines
    """
    text = ""
    with open(filename, "r", newline=None) as fd:
        for line in fd:
            line = line.rstrip('\n')
            text += line

    return(text)

def tokenize(text):
    lst = re.split(r'(\s)', text)
    return ' '.join(lst).split()

def remove_non_alphanumeric(text):
    """ 
    Given: a list of tokens
    For every token remove every token that contains more than one non-alphanumeric character
    except for those where it’s at the end of the word.
    """
    ret = []
    for token in text:
        match = re.search("\W$", token)
        if match:
            ret.append(token)
        elif not re.search(".*\W.*\W.*", token):
            ret.append(token)
    return ret

def remove_numbers(text):
    ret = [token for token in text if not token.isnumeric()]
    return ret

def remove_uppers(text):
    ret = [token for token in text if not token.isupper()]
    return ret

def remove_mixed(text):
    ret = [token for token in text if token.islower() or token.istitle()]
    return ret

def write_to_string(text):
    """
    input: a list
    output: a combined list, separated by spaces
    """
    return " ".join(text)

def do_process(directory, filename):
    out = read_and_strip(directory + filename)
    out = tokenize(out)
    out = remove_non_alphanumeric(out)
    out = remove_numbers(out)
    out = remove_uppers(out)
    out = remove_mixed(out)
    out = write_to_string(out)
    with open(filename + ".clean", 'w') as f:
        f.write(out)

def main():
    do_process("target-corpus-sample/", "argosy-1917.txt")
    

if __name__== "__main__":
  main()

