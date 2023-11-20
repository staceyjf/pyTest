# In this kata you are required to, given a string, replace every letter with its position in the alphabet.

# If anything in the text isn't a letter, ignore it and don't return it.

# def alphabet_position(text):
#     alphabet = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8, "i": 9, "j": 10, "k": 11, "l": 12, "m": 13, "n": 14, "o": 15, "p": 16, "q": 17, "r": 18, "s": 19, "t": 20, "u": 21, "v": 22, "w": 23, "x": 24, "y": 25, "z": 26}
#     clean_text = text.lower().replace(" ", "")
#     result = ""
#     for char in clean_text:
#         if char.isalpha():  # Check if the character is a letter
#             result += str(alphabet.get(char)) + " "
#     return result.strip()  # remove the end space


def alphabet_position(text):
    alphabet = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8, "i": 9, "j": 10, "k": 11, "l": 12, "m": 13, "n": 14, "o": 15, "p": 16, "q": 17, "r": 18, "s": 19, "t": 20, "u": 21, "v": 22, "w": 23, "x": 24, "y": 25, "z": 26}
    clean_text = ''.join(char.lower() for char in text if char.isalpha()) #if letter, make lowercase and concat to new str without spaces
    result = ' '.join(str(alphabet.get(char)) for char in clean_text) #find the value of the relevant key and concat to result with a space
    return result
