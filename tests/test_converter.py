import pytest

from src.converter import convert_number_to_numeral, convert_numeral_to_number


@pytest.mark.parametrize("number,expected_numeral", [
    (0, ""),
    (1, "I"),
    (2, "II"),
    (3, "III"),
    (4, "IV"),
    (5, "V"),
    (6, "VI"),
    (7, "VII"),
    (8, "VIII"),
    (9, "IX"),
    (10, "X"),
    (20, "XX"),
    (30, "XXX"),
    (40, "XL"),
    (100, "C"),
    (200, "CC"),
    (300, "CCC"),
    (400, "CD"),
    (1000, "M"),
    (2000, "MM"),
    (3000, "MMM"),
    (499, "CDXCIX"),
    (3999, "MMMCMXCIX"),
    (1066, "MLXVI"),
    (1989, "MCMLXXXIX")
])
def test_should_convert_number_to_numeral(number, expected_numeral):
    assert convert_number_to_numeral(number) == expected_numeral


@pytest.mark.parametrize("numeral,expected_number", [
    ("", 0),
    ("I", 1),
    ("II", 2),
    ("III", 3),
    ("X", 10),
    ("XX", 20),
    ("XXX", 30),
    ("C", 100),
    ("CC", 200),
    ("CCC", 300),
    ("V", 5)
])
def test_should_convert_numeral_to_number(numeral, expected_number):
    assert convert_numeral_to_number(numeral) == expected_number
