import string


ALPHABET = list(string.ascii_lowercase)
MORSE_CODE = ['o ---', '--- o o o', '--- o --- o', '--- o o', 'o', 'o o --- o', '--- --- o', 'o o o o', 'o o',
              'o --- --- ---', '--- o ---', 'o --- o o', '--- ---', '--- o', '--- --- ---', 'o --- --- o',
              '--- --- o ---', 'o --- o', 'o o o', '---', 'o o ---', 'o o o ---', 'o --- ---', '--- o o ---',
              '--- o --- ---', '--- --- o o']


def convert_to_morse(text):
    morse_text = ''
    for letter in text:
        if letter == " ":
            morse_text += "       " # seven unit space per word
        else:
            morse_text += (MORSE_CODE[ALPHABET.index(letter)] + '   ') # letter + three unit space
    return morse_text


user_text = input("Write something: ")


print(convert_to_morse(user_text))

