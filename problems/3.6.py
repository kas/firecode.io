# 3.6 Excel Spreadsheet - Column Number to Column Name

def excel_column_number_to_name(column_number):
    output = ''

    index = column_number - 1

    while index >= 0:
        character = chr((index % 26) + ord('A'))

        output = output + character

        index = (index / 26) - 1

    return output[::-1]

