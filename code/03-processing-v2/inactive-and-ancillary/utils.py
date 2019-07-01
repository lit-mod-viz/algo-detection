def write_lines_to_file(text, filepath, extension):
    with open (filepath + extension, 'w') as f:
        f.writelines(text)

def read_file(directory, filename):
	with open(directory + filename, 'r') as fp:
		text = fp.read()
	return text
