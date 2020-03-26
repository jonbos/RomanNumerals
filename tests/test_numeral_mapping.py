import pytest

from src.numeral_mapping import get_decimal_value_from_numeral


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
