# Entry point for the Wordle game application

from src.wordle import Wordle

# Initialize the Wordle game with English and Persian word frequency files
wordle = Wordle(file_path_en='src/data/words_frequency.txt',    # English words frequency file
                fila_path_fa='src/data/persian-wikipedia.txt'   # Persian words frequency file
                )


# Run the game (set rtl_support=True for Persian RTL support)
wordle.run(rtl_support=False)
