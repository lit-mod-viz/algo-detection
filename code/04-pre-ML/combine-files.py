# -*- coding: utf-8 -*-
import glob
from datetime import datetime

def logging(x):
	tex="logged: "+x+" on "+str(datetime.today().ctime())
	with open('combine-files-logger.txt','a') as f:
		f.write(tex)
		f.write("\n")

def combine(source,dest):
    files = glob.glob(source+'/*algo-suspected.txt')
    combined_txt = ''
    for file in files:
    	logging('opened file'+file+' ')
    	with open(file,'r') as in_file:
    		txt = in_file.read()
    	combined_txt = combined_txt + txt
    logging('opened all files')
    with open(dest+'combined-test-corpus.txt',"w") as out_file:  
    	out_file.write('%s' % combined_txt)
    logging('finished writing to new file')

src = '../../corpus/project-v2-corpus/'

dst = '../../corpus/project-v2-corpus/'
combine(src,dst)
logging('successfully combined files')