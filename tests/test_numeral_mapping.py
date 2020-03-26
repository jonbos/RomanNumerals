import pytest

from src.numeral_mapping import get_numeral_from_decimal_value, get_decimal_value_from_numeral


@pytest.mark.parametrize("decimal,expected_numeral", [
    (1, "I"),
    (5, "V"),
    (10, "X"),
    (50, "L"),
    (100, "C"),
    (500, "D"),
    (1000, "M")
])
def test_should_return_numeral_from_decimal_value_decimal_place(decimal, expected_numeral):
    assert get_numeral_from_decimal_value(decimal) == expected_numeral


@pytest.mark.parametrize("numeral, expected_decimal", [
    ("I", 1),
    ("V", 5),
    ("X", 10),
    ("L", 50),
    ("C", 100),
    ("D", 500),
    ("M", 1000)
])
def test_should_return_decimal_value_from_numeral(numeral, expected_decimal):
    assert get_decimal_value_from_numeral(numeral) == expected_decimal
