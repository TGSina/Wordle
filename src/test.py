from src.utils import generate_word_freq_fa

import arabic_reshaper
from bidi.algorithm import get_display

fa_path = './src/data/persian-wikipedia.txt'

faword_list = generate_word_freq_fa(fa_path)

# for RTL Persian text support in some terminals:
for i in range(len(faword_list)):
    reshaped_text = arabic_reshaper.reshape(faword_list[i])
    bidi_text = get_display(reshaped_text)
    faword_list[i] = bidi_text


print(faword_list[0:10])
