numerals = {1: "I", 10: "X"}


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
#     10: [10]
# }
def number_to_numeral(number):
    if (number < 10):
        return numerals[1] * number;
    else:
        return numerals[10] * (number // 10)
