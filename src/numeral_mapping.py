from src.util import search_dict_for_value
number_to_numeral = {
    1: "I",
    5: "V",
    10: "X",
    50: "L",
    100: "C",
    500: "D",
    1000: "M"
}

def get_decimal_value_from_numeral(numeral):
    val = search_dict_for_value(number_to_numeral, numeral)
    return val[0]


def get_numeral_from_decimal_value(decimal):
    return number_to_numeral[decimal]
