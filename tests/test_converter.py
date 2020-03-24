import pytest

from src.converter import number_to_numeral


@pytest.mark.parametrize("number,expected_numeral", [
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
])
def test_should_convert_number_to_numeral(number, expected_numeral):
    assert number_to_numeral(number) == expected_numeral
