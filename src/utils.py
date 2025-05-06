# defining colored prints:
from termcolor import colored

def print_valid(txt, end="\n"):
    print(colored(f' {txt} ', 'green', attrs=['reverse', 'bold']), end=end)

def print_position_invalid(txt, end="\n"):
    print(colored(f' {txt} ', 'blue', attrs=['reverse', 'bold']), end=end)

def print_invalid(txt, end="\n"):
    print(colored(f' {txt} ', 'grey', attrs=['reverse', 'bold']), end=end)


# Building general data:
def generate_word_freq(file_path, word_count: int = 5, limit: int = 1000):
    words_list_freq = []

    with open(file_path) as file:
        for line in file:
            # print(line.strip())
            word, freq = line.strip().split(', ')
            freq = int(freq)
            words_list_freq.append((word, freq))


    # Filtering data with word_count:

    words_list_freq = list(filter(lambda w: len(w[0]) == word_count, words_list_freq))

    # Sorting data with limit:

    words_list_freq = sorted(words_list_freq, key=lambda w: w[1], reverse=True)

    # Limit data:

    words_list_freq = words_list_freq[:limit]

    # Drop frequency of words data

    words = [word[0] for word in words_list_freq ]

    return words
