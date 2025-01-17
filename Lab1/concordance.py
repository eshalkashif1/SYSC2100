"""
SYSC 2100 Winter 2024
Lab 1, Part 3, Exercise 4, Extra-Practice Exercise 5
"""

__author__ = 'Eshal Kashif'
__student_number__ = '101297950'

import string

# For information about the string module, type help(string) at the shell
# prompt, or browse "The Python Standard Library", Section "Built-in Types",
# Subsection "Text Sequence Type - str" in the documentation
# (available @ python.org).


def build_concordance(filename: str) -> dict[str, list[int]]:
    """Return a concordance of words in the text file
    with the specified filename.

    The concordance is stored in a dictionary. The keys are the words in the
    text file. The value associated with each key is a list containing the line
    numbers of all the lines in the file in which the word occurs.)

    >>> concordance = build_concordance('sons_of_martha.txt')
    """
    # Open file and declare variables
    infile = open(filename, "r")
    hist = {}
    line_number = 0

    # Separate words in each line
    for line in infile:
        line_number += 1  # Keep track of line number
        word_list = line.split()
        for word in word_list:
            word = word.strip(string.punctuation).lower()
            if word != '':
                # Check if word is in dict and add line number
                if word not in hist:
                    hist[word] = []
                if line_number not in hist[word]:
                    hist[word].append(line_number)

    return hist


# Extra-Practice: Exercise 5 Solution


if __name__ == '__main__':
    # Testing using Two Cities Text
    concordance = build_concordance('two_cities.txt')
    print('Two Cities: ', concordance)

    # Testing using Sons of Martha Text
    concordance2 = build_concordance('sons_of_martha.txt')
    print('Sons of Martha: ', concordance2)

    # Write your solution to Extra-practice Exercise 5 here
