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
    val = _search_dict_for_value(number_to_numeral, numeral)
    return val[0]


def _search_dict_for_value(dict, value):
    if (value in dict.values()):
        return [key for key, val in dict.items() if val == value]
