import math

# 
# 
def split_number_into_powers_of_ten(number):
    """
    Splits an integer into an array of integers represnting each power of ten part
    1234 -> [1000, 200, 30, 4]
    """
    number_digits = [int(digit) for digit in str(number)]
    digits_and_powers_of_ten = zip(number_digits, range(len(number_digits) - 1, -1, -1))
    orders_of_ten = []
    for digit_tuple in digits_and_powers_of_ten:
        digit = digit_tuple[0] * (10 ** digit_tuple[1])
        if digit > 0:
            orders_of_ten.append(digit)
    return orders_of_ten


def calculate_power_of_ten(number):
    return math.floor(math.log10(number))
