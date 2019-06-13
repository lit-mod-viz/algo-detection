def remove_solos(filepath):
    ret = []
    for line in open(filepath, 'r'):
        if len(line.split()) > 1:
            ret.append(line)
    obj = " ".join(ret)
    with open (filepath + ".nosolos", 'w') as f:
        f.write(obj)
    return obj

def main():
    filename = "argosy-1917.txt.clean.segmented"
    obj = remove_solos("output/" + filename)
   

if __name__== "__main__":
  main()