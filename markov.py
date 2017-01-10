from random import choice


def open_and_read_file(file_path):
    """Takes file path as string; returns text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    read_all_file = open(file_path).read()


    return read_all_file


def make_chains(text_string):
    """Takes input text as string; returns _dictionary_ of markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> make_chains("hi there mary hi there juanita")
        {('hi', 'there'): ['mary', 'juanita'], ('there', 'mary'): ['hi'], ('mary', 'hi': ['there']}
    """

    chains = {}

    word_list = open_and_read_file(text_string).split()

    for i in range(len(word_list) - 2):
        first_word = word_list[i]
        second_word = word_list[i+1]
        value = [word_list[i+2]]
        key_pair = (first_word, second_word)
        if key_pair not in chains:
            chains[key_pair] = [value]
        else:
            chains[key_pair].append(value)
    return chains


print make_chains("green-eggs.txt")

def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""

    text = ""
    for key in chains:
        current_key = key
        chosen_word = random.choice(chains[key])
        new_key = (curren_key[1], chosen_word)
        if new_key in chains:
            new_rand_word = random.choice(chains[new_key])
        else:
            break
    return text


input_path = "green-eggs.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print random_text
