# 1.4 Binary Representation

def dec_to_bin(number):
    if number < 2:
        return str(number)

    return dec_to_bin(number / 2) + str(number % 2)

