import math

numerals = {1: "I",
            5: "V",
            10: "X",
            100: "C",
            1000: "M"
            }

mapping = {
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


def number_to_numeral(number):
    res = ""
    power_of_ten = floor_log_10(number)
    pattern = mapping[number // 10 ** power_of_ten]

    for numeral in pattern:
        print(numeral, 10 ** power_of_ten)
        res += numerals[numeral * (10 ** power_of_ten)]
    return res


def floor_log_10(number):
    return math.floor(math.log10(number))
