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


def generate_word_freq_fa(file_path, word_count: int = 5, limit: int = 1000, ignore_lines: int = 20):
    """
    Generates Persian words from a given .txt file, based on words frequencies.
    """

    # Extract words and their frequencies in a list of tuples:
    with open(file_path) as file:
        counter = 0
        faword_freq_list = []
        
        for line in file:
            counter += 1
            if counter <= ignore_lines:
                continue
    
            faword, freq = line.strip().split()
            freq = int(freq)
            faword_freq_list.append((faword, freq))

    # Filtering based on word_count
    faword_freq_list = list(filter(lambda w: len(w[0]) == word_count, faword_freq_list))

    # Sorting words based on frequencies
    faword_freq_list = sorted(faword_freq_list, key=lambda w: w[1], reverse=True)

    # Keep the most common words with limit
    faword_freq_list = faword_freq_list[0:limit]

    # Drop frequencies and return the words list
    fa_words = [w[0] for w in faword_freq_list]

    return fa_words
