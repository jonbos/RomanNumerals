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
    return [dec for dec, numer in number_to_numeral.items() if numer == numeral][0]


def get_numeral_from_decimal_value(decimal):
    return number_to_numeral[decimal]


def get_valid_numeral_characters():
    return "".join(number_to_numeral.values())


def calculate_max_representable_number():
    return (4 * max(number_to_numeral.keys()) - 1)
