# Wordle (English & Persian)

A command-line Wordle game supporting both English and Persian (Farsi) languages, with right-to-left (RTL) support for Persian.
Guess the hidden word in a limited number of tries!

## Features

- Play Wordle in English or Persian
- Colored feedback for correct, misplaced, and wrong letters
- Persian RTL support (with optional libraries)
- Customizable word length and number of tries
- Uses frequency lists for meaningful word selection

## Demo

```bash
Choose your game language (en/fa): en
This is your 1 chance, to enter a 5 length word (or enter q to exit): apple
A P P L E
You won hero! The word was APPLE
```

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/TGSina/Wordle.git
   cd wordle
   ```

2. **(Optional) Create a virtual environment:**

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies:**

      ```bash
      pip install -r requirements.txt
      ```

      *If you want Persian RTL support, make sure `bidi` and `arabic-reshaper` are included in `requirements.txt`.*

## Usage

Run the game from the `src` directory:

```bash
python src/main.py
```

- Choose `en` for English or `fa` for Persian.
- For Persian, you can enable RTL support by editing `main.py`:

  ```python
  wordle.run(rtl_support=True)
  ```

## Project Structure

```text
src/
  main.py         # Entry point for the game
  wordle.py       # Main game logic (Wordle class)
  utils.py        # Utility functions (color printing, RTL handling)
  data/
    words_frequency.txt         # English words and frequencies
    persian-wikipedia.txt       # Persian words and frequencies
    rira-classic-poems.txt      # (Optional) Persian poetry dataset
```

- **main.py**: Starts the game, sets up the Wordle object.
- **wordle.py**: Contains the `Wordle` class, game logic, word list loading, and user interaction.
- **utils.py**: Helper functions for colored output and RTL text.

## Customization

- **Change word length or tries:**
  Edit the `Wordle` initialization in `main.py`:

  ```python
  wordle = Wordle(file_path_en=..., fila_path_fa=..., word_len=5, num_try=6)
  ```

- **Add your own word lists:**
  Replace or edit the files in `src/data/`.

## Requirements

- Python 3.7+
- For Persian RTL support:
  - `bidi`
  - `arabic-reshaper`
- See `requirements.txt` for all dependencies.

## Contributing

Pull requests and suggestions are welcome!  
Please open an issue for bugs or feature requests.
