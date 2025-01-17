"""
SYSC 2100 Winter 2024
Lab 1, Part 2, Exercises 2 and 3
Case study: a function that uses Python's str, list, tuple set and dict
abstract data types.
"""

__author__ = 'Eshal Kashif'
__student_number__ = '101297950'

import string

# For information about the string module, type help(string) at the shell
# prompt, or browse "The Python Standard Library", Section "Built-in Types",
# Subsection "Text Sequence Type - str" in the Python documentation
# (available @ python.org).


"""
ANSWERS TO QUESTIONS

Exercise 2, Step 2
Which word occurs most frequently in the file? How often does it occur?
--> the; 42
"""


def build_histogram(filename: str) -> dict[str, int]:
    """Return a histogram of the words in the text file with the specified name.

    The histogram is a collection of counters. Each counter keeps track of the
    number of occurrences of one word.

    The histogram is stored in a dictionary.The keys are the words in the text
    file. The value associated with each key is the number of occurrences of
    that word.

    >>> hist = build_histogram('sons_of_martha.txt')
    >>> hist
    >>> len(hist)  # How many different words are in the file? 249
    """
    infile = open(filename, "r")
    hist = {}

    for line in infile:

        # Split each line into a list of words.
        # By default, the split method removes all whitespace; e.g.,
        # '  Hello,    world!   '.split() returns this list:
        #
        #    ['Hello,', 'world!']
        #
        # and not:
        #
        #    ['  Hello,', '    world!   ']
        #
        # Notice that the punctuation marks have not been removed.

        word_list = line.split()

        # For each word, first remove any leading or trailing punctuation,
        # then convert the the word to lower case.
        #
        # Examples:
        #  'Hello,'.strip(string.punctuation) returns 'Hello'.
        #  'Hello'.lower() returns 'hello'.

        for word in word_list:
            word = word.strip(string.punctuation).lower()

            # or,
            # word = word.strip(string.punctuation)
            # word = word.lower()

            # Increment the counter that counts the number of times
            # word is in the file.
            # Don't count any empty strings that are created when punctuation
            # marks are removed.
            # For example, if variable word is a hyphen, '-',
            # word.strip(string.punctuation) returns the empty string, ''.

            if word != '':
                count = hist.get(word, 0)  # get returns the current count of
                # the number of occurrences of word,
                # or 0 if word is not yet in the
                # dictionary.
                hist[word] = count + 1

            # or simply,
            # hist[word] = hist.get(word, 0) + 1

    return hist


def most_frequent_word(hist: dict[str, int]) -> tuple[str, int]:
    """Return a tuple containing the most frequently occurring word in the
    specified histogram (a dictionary of word/occurrence count pairs),
    along with its frequency.

    >>> hist = build_histogram('sons_of_martha.txt')
    >>> hist
    >>> len(hist)  # How many different words are in the file? 249
    >>> most_frequent_word(hist)  # Which word occurs most often? the
    """
    frequency = -1
    for word in hist:
        if hist[word] > frequency:
            frequency = hist[word]
            most_frequent = word

    return (most_frequent, frequency)


def words_with_frequency(hist: dict[str, int], n: int) -> list[str]:
    """Returns a list of all words in histogram hist that occur with
    frequency n. The list is sorted in ascending order.

    >>> hist = build_histogram('sons_of_martha.txt')
    >>> words_with_frequency(hist, 1)  # Which words occur once in the file?
    >>> words_with_frequency(hist, 5)  # Which words occur five times?
    """
    # Write your code for Exercise 3 here.
    word_list = []
    # Iterate through each word in dict
    for word in hist:
        if hist[word] == n:  # Check if frequency is equal to specified value
            word_list.append(word)

    word_list.sort()

    return word_list


if __name__ == '__main__':
    # Build and display a histogram of the distinct words in a file
    filename = 'sons_of_martha.txt'
    hist = build_histogram(filename)
    print('File', filename, 'contains', len(hist), 'distinct words')
    print('The histogram is:', hist)

    # Write your code for Exercise 2, Step 5, here.
    most_common_word = most_frequent_word(hist)
    print('The most frequently occurring word is: ', most_common_word[0])
    print('# of occurrences: ', most_common_word[1])
    # Most common word is the, appears 42 times

    # Testing Excercise 3
    hist2 = build_histogram('two_cities.txt')
    print('\nWords with occurance of 1: ', words_with_frequency(hist2, 1))
    print('Words with occurance of 2: ', words_with_frequency(hist2, 2))
    print('Words with occurance of 3: ', words_with_frequency(hist2, 3))

    print('\nTesting Sons of Martha Text')
    print('Words with occurance of 42: ', words_with_frequency(hist, 42))
    print('Words with occurance of 1: ', words_with_frequency(hist, 1))
    print('Words with occurance of 5: ', words_with_frequency(hist, 5))

