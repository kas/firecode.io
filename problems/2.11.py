# 2.11 Unique Chars in a String

def unique_chars_in_string(input_string):
    dictionary = {}

    for character in input_string:
        if character in dictionary:
            return False
        else:
            dictionary[character] = 1

    return True
