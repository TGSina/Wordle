from src.wordle import Wordle

wordle = Wordle(file_path_en='src/data/words_frequency.txt',
                fila_path_fa='src/data/persian-wikipedia.txt'
                )

# print(wordle.words)
wordle.run()


# https://github.com/behnam/persian-words-frequency
