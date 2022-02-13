"""Generate Markov text from text files."""

from random import choice
import sys

def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # your code goes here
    file = open(file_path)
    one_string = file.read().strip()

          

    return one_string


def make_chains(text_string, N):
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
    
    
    
    words = text_string.split()
    n = N
    for i in range(len(words) - n):
        key_n_words_list = []
        for p in range(n):
            key_n_words_list.append(words[i + p])
        key_n_words = tuple(key_n_words_list)
        
        if chains.get(key_n_words) == None:
            chains[key_n_words] = [words[i+n]]
        else:
            chains[key_n_words].append(words[i+n])
    
         

    
    return chains


def make_text(chains, N):
    """Return text from chains."""

    flag = True
    while flag:
        start_key = choice(list(chains.keys()))
        if str(start_key[0][0]).isupper():
            flag = False
    


    n = N
    words = list(start_key)
    new_key = start_key
    
    while words[-1].isalpha():
               
               
        word_nrd = choice(chains[new_key])
        words.append(word_nrd)
        if words[-1].isalpha() == False:
            break
        
        new_key = tuple(words[-n:])

        if chains.get(new_key) == None:
            break  
        
        words[len(words):] = list(new_key)
            


    return ' '.join(words)


input_path = sys.argv[1]
n = int(input("Please enter an integer: "))

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text, n)

# Produce random text
random_text = make_text(chains, n)


print(random_text)
