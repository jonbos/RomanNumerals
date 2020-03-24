import pytest

from src.number_util import split_int_into_factors_of_ten


@pytest.mark.parametrize("number,expected_array", [
    (1, [1]),
    (10, [10]),
    (11, [10, 1]),
    (499, [400, 90, 9]),
    (400, [400]),
    (1234, [1000, 200, 30, 4])
])
def test_should_split_number_on_decimal_place(number, expected_array):
    assert split_int_into_factors_of_ten(number) == expected_array
