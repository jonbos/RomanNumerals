import math

def split_number_into_orders_of_ten(number):
    number_digits = [int(digit) for digit in str(number)]
    digits_and_powers_of_ten = zip(number_digits, range(len(number_digits) - 1, -1, -1))
    orders_of_ten = []
    for digit_tuple in digits_and_powers_of_ten:
        digit = digit_tuple[0] * (10 ** digit_tuple[1])
        if digit > 0:
            orders_of_ten.append(digit)
    return orders_of_ten


def floor_log_10(number):
    return math.floor(math.log10(number))


def search_dict_for_value(dict, value):
    if (value in dict.values()):
        return [key for key, val in dict.items() if val == value]
