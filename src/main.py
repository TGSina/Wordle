from src.wordle import Wordle

wordle = Wordle(file_path_en='src/data/words_frequency.txt',    # English words frequency file
                fila_path_fa='src/data/persian-wikipedia.txt'   # Persian words frequency file
                )


wordle.run(rtl_support=False) # or wordle.run(rtl_support=True) for RTL support if needed

