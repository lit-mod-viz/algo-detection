# -*- coding: utf-8 -*-
import glob
import argparse
from datetime import datetime

def logging(x):
	tex="logged: "+x+" on "+str(datetime.today().ctime())
	with open('combine-files-logger.txt','a') as f:
		f.write(tex)
		f.write("\n")

def combine(source, out_file, extension):
    files = glob.glob(source + '*' + extension)
    combined_txt = ''
    for file in files:
    	logging('opened file'+file+' ')
    	with open(file,'r') as in_file:
    		txt = in_file.read()
    	combined_txt = combined_txt + txt
    logging('opened all files')
    with open(out_file,"w") as out_file:  
    	out_file.write('%s' % combined_txt)
    logging('finished writing to new file')


def main():
    parser = argparse.ArgumentParser(description='parse arguments')
    parser.add_argument('source_directory', type=str, help='file to read')
    parser.add_argument('out_file', type=str, help='output file')
    parser.add_argument('extension', type=str, help='types of files to combine')

    args = parser.parse_args()
    combine(args.source_directory, args.out_file, args.extension)
    logging('successfully combined files')

if __name__== "__main__":
  main()


