import pytest

from src.number_util import split_on_decimal_place


@pytest.mark.parametrize("number,expected_array", [
    (1, [1]),
])
def test_should_convert_number_to_numeral(number, expected_array):
    assert split_on_decimal_place(number) == expected_array
