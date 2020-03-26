decimal_digit_to_numeral_pattern = {
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


def get_numeral_pattern_from_decimal_digit(number):
    return decimal_digit_to_numeral_pattern[number];
