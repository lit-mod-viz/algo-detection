import re
from utils import *
from no_solos import read_file_to_list, make_lower, remove_punctuation, remove_hyphens
from clean import remove_uppers

def trim_file(text):
	l = re.split(r'([\d]+[.])', text)
	nums = re.findall(r'([\d]+[.])', text)
	diff = [item for item in l if item not in nums]
	nested = [sent.split('\n\n') for sent in diff]
	cleaned = []
	d = []
	for l in nested:
		cleaned.append([item.rstrip().lstrip() for item in l])
	# get rid of blank lists and blank strings
	for l in cleaned:
		sub = [item for item in l if item]
		if sub: d.append(sub)
	return(d)

def fill_sentences(textlist):
	bigret = []
	for sublist in textlist:
		subret = []
		temp = sublist[0]
		for line in sublist[2:]:
			subret.append(temp + " " + line)
		bigret.append(subret)
	ret = [item + "\n" for sublist in bigret for item in sublist]
	return ret

def strip_numbers_from_sentence(textlist):
	ret = []
	for string in textlist:
		ret.append(''.join(i for i in string if not i.isdigit()))
	return ret

def fix_enjambment(text):
	textlist = text.split("\n\n")
	ret = [re.sub(r'\n', '', sentence) for sentence in textlist]
	return ret

def remove_extraneous_spaces(textlist):
	return [re.sub(' +', ' ', sentence) for sentence in textlist]

def append_newlines(textlist):
	return [sentence + "\n" for sentence in textlist]

def strip_bookending_whitespace(textlist):
	return [sentence.lstrip().rstrip() for sentence in textlist]

def remove_between_parens(textlist):
	return [re.sub(r'\([^)]*\)', '', sentence) for sentence in textlist]

def main():
	directory = "../source-corpus-pared/clean-data/plotto/"
	filename = "plotto.txt"
	text = read_file(directory, filename)
	obj = fix_enjambment(text)
	obj = remove_between_parens(obj)
	obj = remove_hyphens(obj)
	obj = strip_numbers_from_sentence(obj)
	obj = remove_punctuation(obj)
	obj = strip_bookending_whitespace(obj)
	obj = append_newlines(obj)
	print(obj)
	write_lines_to_file(obj, "output/source-output/" + filename, ".stripped")

if __name__ == "__main__":
    main()