import pytest

from src.converter import number_to_numeral


@pytest.mark.parametrize("number,expected_numeral", [
    (1, "I"),
    (2, "II"),
    (3, "III"),
    (10, "X"),
    (20, "XX"),
    (30, "XXX")
])
def test_should_convert_number_to_numeral(number, expected_numeral):
    assert number_to_numeral(number) == expected_numeral
