import math


def to_roman(num):
    # write your code here!
    # start by defining a dictionary with key/value as roman numeral: arabic equivalent from greatest to least

    # create an empty string here as placeholder for our final romanNumeral
    final_num = ""
    arabic_dictionary = {
        "I": 1,
        "IV": 4,
        "V": 5,
        "IX": 9,
        "X": 10,
        "XL": 40,
        "L": 50,
        "XC": 90,
        "C": 100,
        "CD": 400,
        "D": 500,
        "CM": 900,
        "M": 1000
    }

    # create a list of the roman numerals from greatest to least
    roman_nums = ['M', 'CM', 'D', 'CD', 'C', 'XC',
                  'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
    # establish a for loop of the items in the list
    for item in roman_nums:
        divided_num = math.floor(num / arabic_dictionary[item])
        for x in range(0, divided_num):
            final_num = final_num + item
            num = num - arabic_dictionary[item]

    return final_num


print(to_roman(4))
print(to_roman(11))
print(to_roman(14))
print(to_roman(16))
print(to_roman(1437))
# TEST CASES
