import pytest

from src.converter import number_to_numeral


@pytest.mark.parametrize("number,expected_numeral", [
    (1, "I"),
    (2, "II"),
    (3, "III"),
    (10, "X"),
    (20, "XX"),
    (30, "XXX"),
    (100, "C"),
    (200, "CC"),
    (300, "CCC"),
    (1000, "M"),
    (2000, "MM"),
    (3000, "MMM"),
    (5, "V"),
    (4, "IV")
])
def test_should_convert_number_to_numeral(number, expected_numeral):
    assert number_to_numeral(number) == expected_numeral


