#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or type(roman_string) is not str:
        return 0
    if roman_string == "":
        return 0
    number = 0
    dictionary = {"I": 1, "V": 5, "X": 10,
                  "L": 50, "C": 100, "D": 500, "M": 1000}
    for i, j in zip(roman_string, roman_string[1:]):
        if i not in dictionary.keys():
            return 0
        elif dictionary[i] >= dictionary[j]:
            number += dictionary[i]
        else:
            number -= dictionary[i]
    number += dictionary[roman_string[-1]]
    return number
