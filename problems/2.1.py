# 2.1 Insert Stars

def insert_star_between_pairs(a_string):
    # base case
    if (not a_string) or (len(a_string) == 1):
        return a_string

    if a_string[0] == a_string[1]:
        return a_string[0] + '*' + insert_star_between_pairs(a_string[1:len(a_string)])
    else:
        return a_string[0] + insert_star_between_pairs(a_string[1:len(a_string)])
