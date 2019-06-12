def remove_solos(filename):
    ret = []
    for line in open(filename, 'r'):
        if len(line.split()) > 1:
            ret.append(line)
    return " ".join(ret)

def main():
    filename = "argosy-1917.txt.clean.segmented"
    obj = remove_solos(filename)
    with open (filename + ".nosolos", 'w') as f:
        f.write(obj)

if __name__== "__main__":
  main()