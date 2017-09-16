# 2.14 Power of 4

def is_power_of_four(number):
    if number and not (number & (number - 1)):
        count = 0

        while number > 1:
            number >>= 1
            count += 1

        return (count % 2) == 0

    return False

