import os

from symspellpy import SymSpell, Verbosity  # import the module

def fix_spelling(directory, filename):
    # maximum edit distance per dictionary precalculation
    max_edit_distance_dictionary = 2
    prefix_length = 7
    # create object
    sym_spell = SymSpell(max_edit_distance_dictionary, prefix_length)
    # load dictionary
    dictionary_path = os.path.join(os.path.dirname(__file__), "frequency_dictionary_en_82_765.txt")
    term_index = 0  # column of the term in the dictionary text file
    count_index = 1  # column of the term frequency in the dictionary text file
    if not sym_spell.load_dictionary(dictionary_path, term_index, count_index):
        print("Dictionary file not found")
        return

    # max edit distance per lookup (per single word, not per whole input string)
    max_edit_distance_lookup = 2
    corrected_list = []
    for line in open(directory + filename, 'r'):
        suggestions = sym_spell.lookup_compound(line, max_edit_distance_lookup)
        for suggestion in suggestions:
            corrected_list.append(suggestion.term)
    print(corrected_list)
    # text = " ".join(corrected_list)
    with open("output/" + filename + ".spell", 'w') as f:
        for line in corrected_list:
            f.write(line)
            f.write('\n')            

def main():
    fix_spelling("output/", "argosy-1917.txt.clean.segmented.nosolos-nohyphens")

if __name__ == "__main__":
    main()