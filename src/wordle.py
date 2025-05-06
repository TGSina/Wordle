import random
# random.seed(42)

from src.utils import print_invalid, print_position_invalid, print_valid

class Wordle:
    def __init__(self, file_path: str, word_len: int = 5, limit: int = 1_000, num_try: int = 5):
        self.word_count = word_len
        self.num_try = num_try
        self.words = self.generate_word_freq(file_path, word_count=word_len, limit=limit)


    # Building general data:
    def generate_word_freq(self, file_path, word_count, limit):
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


    def run(self, ):
        # generate answer
        answer_word = random.choice(self.words).upper()

        # start game
        # num_try = 7
        try_num = 1

        while True:
            guess = input(f'This is your {try_num} chance, to enter a {self.word_count} length word (or enter q to exit):  ').upper()

            if guess.lower() == "q":
                break

            # checking word length:
            if len(guess) != self.word_count:
                print("wrong word length! try again.")
                continue

            # checking if input is a meaningful word:
            if guess.lower() not in self.words:
                print("Not a word! try again:")
                continue

            # check input with answer:
            for g_letter, a_letter in zip(guess, answer_word):
                # print(g_letter, a_letter)
                if g_letter == a_letter:
                    print_valid(g_letter, end=" ")
                elif g_letter in answer_word:
                    print_position_invalid(g_letter, end=" ")
                else:
                    print_invalid(g_letter, end=" ")

            print()

            # check the success:
            if guess == answer_word:
                print(' ')
                print_valid(f"You won hero! The word was {answer_word}")
                break

            try_num += 1
            if try_num > self.num_try:
                print(' ')
                print_invalid(f"The word was {answer_word}, sorry you didn't catch it :(")
                break

# if __name__ == '__main__':
#     wordle = Wordle()
#     wordle.run()