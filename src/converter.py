import math

from src.util import split_int_into_factors_of_ten

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


def is_valid(number_or_numeral):
    return number_is_valid(number_or_numeral) or numeral_is_valid(number_or_numeral)


def convert(number_or_numeral):
    if (not is_valid(number_or_numeral)):
        return "Invalid input: " + str(number_or_numeral)

    if (number_is_valid(number_or_numeral)):
        return convert_number_to_numeral(number_or_numeral)
    else:
        return convert_numeral_to_number(number_or_numeral)


def convert_number_to_numeral(number):
    numeral = ""
    number_arr = split_int_into_factors_of_ten(number)

    for factor in number_arr:
        numeral += (_number_to_numeral(factor))

    return numeral


def _number_to_numeral(number):
    numeral = ""
    power_of_ten = floor_log_10(number)
    pattern = patterns[number // 10 ** power_of_ten]
    for digit in pattern:
        numeral += numerals[digit * (10 ** power_of_ten)]
    return numeral


def convert_numeral_to_number(numeral):
    if (not numeral):
        return 0

    numeral = list(numeral)
    current_val = _get_decimal_value_from_numeral(numeral.pop())
    sum = current_val
    while (numeral):
        prev_val = current_val
        current_val = _get_decimal_value_from_numeral(numeral.pop())
        if (current_val < prev_val): current_val = -current_val
        sum += current_val

    return sum


def _get_decimal_value_from_numeral(numeral):
    val = [decimal for decimal, numer in numerals.items() if numer == numeral]
    return val[0]


def numeral_is_valid(numeral):
    numeral_chars = "".join(numerals.values())
    for char in str(numeral):
        if char not in numeral_chars:
            return False
    return True


def number_is_valid(number):
    return type(number) == int and number <= 3999


def floor_log_10(number):
    return math.floor(math.log10(number))
