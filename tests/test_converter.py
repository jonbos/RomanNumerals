import pytest

from src.converter import number_to_numeral

@pytest.mark.parametrize("number,expected_numeral", [(1, "I")])
def test_should_convert_number_to_numeral(number, expected_numeral):
    assert number_to_numeral(number) == expected_numeral
