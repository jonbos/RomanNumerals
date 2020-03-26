from src.numeral_mapping import get_decimal_value_from_numeral, get_numeral_from_decimal_value, number_to_numeral
from src.numeral_patterns import get_numeral_pattern_from_number
from src.util import split_number_into_orders_of_ten, floor_log_10

def convert(number_or_numeral):
    if (is_valid_number(number_or_numeral)):
        return convert_number_to_numeral(number_or_numeral)
    elif (is_valid_numeral((number_or_numeral))):
        return convert_numeral_to_number(number_or_numeral)
    else:
        return "Invalid input: " + str(number_or_numeral)


def convert_number_to_numeral(number):
    numeral = ""

    for power_of_ten in split_number_into_orders_of_ten(number):
        numeral += (_number_to_numeral(power_of_ten))

    return numeral

def _number_to_numeral(number):
    numeral = ""
    order_of_ten = floor_log_10(number)
    decimal_digit = number // 10 ** order_of_ten

    pattern = get_numeral_pattern_from_number(decimal_digit)

    for decimal in pattern:
        numeral += get_numeral_from_decimal_value(decimal * (10 ** order_of_ten))
    return numeral


def convert_numeral_to_number(numeral):
    if (not numeral):
        return 0

    numeral = list(numeral)
    # pop each numeral off the back of the list (effectively reversing the numeral string)
    current_val = get_decimal_value_from_numeral(numeral.pop())
    sum = current_val
    while (numeral):
        prev_val = current_val
        current_val = get_decimal_value_from_numeral(numeral.pop())
        # if the current value is less than the previous value, it should be subtracted from sum
        if (current_val < prev_val): current_val = -current_val
        sum += current_val

    return sum


def is_valid_numeral(numeral):
    numeral_chars = "".join(number_to_numeral.values())
    for char in str(numeral):
        if char not in numeral_chars:
            return False
    return True


def is_valid_number(number):
    return type(number) == int and number <= 3999 and number >= 0
