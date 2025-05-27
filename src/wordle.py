import random
# random.seed(42)

from src.utils import print_invalid, print_position_invalid, print_valid, rtl_text

class Wordle:
    """
    Main Wordle game class.
    Handles game logic, word list generation, and user interaction for both English and Persian.
    """

    def __init__(self, file_path_en: str, fila_path_fa: str, word_len: int = 5, limit: int = 1_000, num_try: int = 5):
        """
        Initializes the Wordle game.
        Loads English and Persian word lists from files.
        """
        
        self.word_count = word_len
        self.num_try = num_try
        self.words_en = self.generate_word_freq_en(file_path_en, word_count=word_len, limit=limit)
        self.words_fa = self.generate_word_freq_fa(fila_path_fa, word_count=word_len, limit=limit)

    # Building general data:
    def generate_word_freq_en(self, file_path, word_count, limit):
        """
        Reads English words and their frequencies from a file.
        Filters and sorts them, then returns a list of words.
        """
        
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

    def generate_word_freq_fa(self, file_path, word_count, limit):
        """
        Reads Persian words and their frequencies from a file.
        Filters and sorts them, then returns a list of words.
        Ignores lines starting with '#' (comments).
        """

        faword_freq_list = []
        # Extract words and their frequencies in a list of tuples:
        with open(file_path) as file:

            for line in file:

                # Ignore the first 20 lines of dataset (which are commented)
                if '#' in line.strip():
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

    def run(self, rtl_support: bool = False):
        """
        Starts the game and asks the user to choose the language.
        """
        while True:
            game_language = input("Choose your game language (en/fa): ").strip().lower()
            if game_language == "fa":
                self.run_fa(rtl_support=rtl_support)
                break
            elif game_language == "en":
                self.run_en()
                break
            else:
                print("Invalid language choice! Please choose 'en' or 'fa'. Try again.")
                continue


    def run_en(self, ):
        """
        Runs the English version of the Wordle game.
        """
    
        # generate answer
        answer_word = random.choice(self.words_en).upper()

        # start game
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
            if guess.lower() not in self.words_en:
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


    def run_fa(self, rtl_support: bool = False):
        """
        Runs the Persian version of the Wordle game.
        Supports right-to-left (RTL) display if enabled.
        """

        # generate answer
        answer_word = random.choice(self.words_fa).upper()

        # start game
        try_num = 1

        while True:

            if rtl_support:
                guess = input(rtl_text(f'این تلاش {try_num}ام شماست، لطفا کلمه‌ای {self.word_count} حرفی را وارد کنید (یا برای خروج حرف خ را وارد کنید):')).upper()
            else:
                guess = input(f'این تلاش {try_num}ام شماست، لطفا کلمه‌ای {self.word_count} حرفی را وارد کنید (یا برای خروج حرف خ را وارد کنید):').upper()

            if guess == "خ":
                break

            # checking word length:
            if len(guess) != self.word_count:
                if rtl_support:
                    print(rtl_text("تعداد حروف اشتباه است، دوباره امتحان کن"))
                else:
                    print("تعداد حروف اشتباه است، دوباره امتحان کن")
                continue

            # # checking if input is a meaningful word:
            # if guess not in words:
            #     print("Not a word! try again:")
            #     continue

            # check input with answer:
            for g_letter, a_letter in zip(guess, answer_word):
                # print(g_letter, a_letter)
                if g_letter == a_letter:
                    if rtl_support:
                        print_valid(rtl_text(g_letter), end=" ")
                    else:
                        print_valid(g_letter, end=" ")
                elif g_letter in answer_word:
                    if rtl_support:
                        print_position_invalid(rtl_text(g_letter), end=" ")
                    else:
                        print_position_invalid(g_letter, end=" ")
                else:
                    if rtl_support:
                        print_invalid(rtl_text(g_letter), end=" ")
                    else:
                        print_invalid(g_letter, end=" ")

            print()

            # check the success:
            if guess == answer_word:
                if rtl_support:
                    print_valid(rtl_text(f"تو بردی قهرمان! کلمه‌ی هدف {answer_word} بود"))
                else:
                    print_valid(f"تو بردی قهرمان! کلمه‌ی هدف {answer_word} بود")
                break

            try_num += 1
            if try_num > self.num_try:
                if rtl_support:
                    print_invalid(rtl_text(f"کلمه‌ی درست {answer_word} بود، انشالله دفعه بعد :("))
                else:
                    print_invalid(f"کلمه‌ی درست {answer_word} بود، انشالله دفعه بعد :(")
                break

# Uncomment to run directly
# if __name__ == '__main__':
#     wordle = Wordle()
#     wordle.run()