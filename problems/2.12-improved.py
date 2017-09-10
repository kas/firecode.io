# 2.12 Unique Chars in a String

def unique_chars_in_string(input_string):
    character_set = set()

    for character in input_string:
        if character in character_set:
            return False
        else:
            character_set.add(character)

    return True

