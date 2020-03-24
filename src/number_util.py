def split_int_into_factors_of_ten(number):
    number_digits = [int(digit) for digit in str(number)]
    digits_and_powers_of_ten = zip(number_digits, range(len(number_digits) - 1, -1, -1))
    res = []
    for digit_tuple in digits_and_powers_of_ten:
        res.append(digit_tuple[0] * (10 ** digit_tuple[1]))
    return res
