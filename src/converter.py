import math

from src.number_util import split_int_into_factors_of_ten

numerals = {
    1: "I",
    5: "V",
    10: "X",
    50: "L",
    100: "C",
    500: "D",
    1000: "M"
}

patterns = {
    0: [],
    1: [1],
    2: [1, 1],
    3: [1, 1, 1],
    4: [1, 5],
    5: [5],
    6: [5, 1],
    7: [5, 1, 1],
    8: [5, 1, 1, 1],
    9: [1, 10]
}


def number_to_numeral(number):
    res = ""
    number_arr = split_int_into_factors_of_ten(number)

    for decimal in number_arr:
        power_of_ten = floor_log_10(decimal)
        pattern = patterns[decimal // 10 ** power_of_ten]
        for numeral in pattern:
            res += numerals[numeral * (10 ** power_of_ten)]
    return res

def floor_log_10(number):
    return math.floor(math.log10(number))
