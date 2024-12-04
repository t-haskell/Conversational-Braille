import time
def text_to_braille(text):
    start = time.time()
    braille_dict = {
        'a': '⠁', 'b': '⠃', 'c': '⠉', 'd': '⠙', 'e': '⠑',
        'f': '⠋', 'g': '⠛', 'h': '⠓', 'i': '⠊', 'j': '⠚',
        'k': '⠅', 'l': '⠇', 'm': '⠍', 'n': '⠝', 'o': '⠕',
        'p': '⠏', 'q': '⠟', 'r': '⠗', 's': '⠎', 't': '⠞',
        'u': '⠥', 'v': '⠧', 'w': '⠺', 'x': '⠭', 'y': '⠽',
        'z': '⠵', ' ': '⠀', ',': '⠂', '.': '⠃', '?': '⠦',
        '!': '⠖', '-': '⠤', '(': '⠣', ')': '⠜', '/': '⠪',
        '1': '⠁', '2': '⠃', '3': '⠉', '4': '⠙', '5': '⠑',
        '6': '⠋', '7': '⠛', '8': '⠓', '9': '⠊', '0': '⠚',
    }
    # TODO: use translation table for str.translate
    # Generate translation table for str.translate
    translation_table = str.maketrans(braille_dict)
    braille = text.lower().translate(translation_table)
    runtime = time.time() - start

    # Use translate for faster conversion
    return braille, runtime
    # braille_text = "".join(braille_dict.get(char, char) for char in text.lower())
    # runtime = time.time() - start

    # return braille_text, runtime
