"""Generate Markov text from text files."""

from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text. as an array
    """

    contents = open(file_path).read()

    return contents
 
text = open_and_read_file('green-eggs.txt')

def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains('hi there mary hi there juanita')

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}

    word_array = text_string.split() 

    for i in range(len(word_array) - 2): 
        #Would you like them, Sam I am?
        #  0   1    2
        #      1    2    3
        #           2    3    4
     # ('Would', 'you'): ['like'],
        key_tuple = word_array[i], word_array[i + 1]
        next_word = word_array[i+2]
        
        if key_tuple in chains:
            chains[key_tuple].append(next_word)
        else:
            chains[key_tuple] = [next_word] 

    for key_tuple, arr in chains.items():
        print(tuple, ":", arr)

make_chains(text)

def make_text(chains):
    """Return text from chains."""

    words = []

    # your code goes here

    return ' '.join(words)


input_path = 'green-eggs.txt'

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)
