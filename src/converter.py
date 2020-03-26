from src.number_util import split_number_into_powers_of_ten, calculate_power_of_ten
from src.numeral_mapping import get_decimal_value_from_numeral, get_numeral_from_decimal_value, number_to_numeral
from src.numeral_patterns import get_numeral_pattern_from_decimal_digit


def convert(number_or_numeral):
    if (is_valid_number(number_or_numeral)):
        return convert_number_to_numeral(number_or_numeral)
    elif (is_valid_numeral((number_or_numeral))):
        return convert_numeral_to_number(number_or_numeral)
    else:
        return "Invalid input: " + str(number_or_numeral)


def convert_number_to_numeral(number):
    numeral = ""

    for order_of_ten_part in split_number_into_powers_of_ten(number):
        numeral += (apply_numeral_pattern_to_decimal_order(order_of_ten_part))

    return numeral


def apply_numeral_pattern_to_decimal_order(number):
    numeral = ""
    power_of_ten = calculate_power_of_ten(number)
    decimal_digit = number // 10 ** power_of_ten

    pattern = get_numeral_pattern_from_decimal_digit(decimal_digit)

    for pattern_digit in pattern:
        numeral += get_numeral_from_decimal_value(pattern_digit * (10 ** power_of_ten))
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
