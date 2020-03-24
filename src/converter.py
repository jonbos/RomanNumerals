numerals = {1: "I", 5: "V", 10: "X", 100: "C", 1000: "M"}

# mapping={
#     1:[1],
#     2:[1,1],
#     3: [1,1,1],
#     4: [1,5],
#     5: [5],
#     6: [5,1],
#     7: [5,1,1],
#     8: [5,1,1,1],
#     9: [1,10],
# }

def number_to_numeral(number):
    magnitude = get_magnitude(number)
    return numerals[magnitude] * (number // magnitude)

def get_magnitude(number):
    decimal = (next(decimal for decimal in reversed(list(numerals)) if number >= decimal))
    return decimal
