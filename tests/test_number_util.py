import pytest

from src.util import split_number_into_orders_of_ten, calculate_order_of_ten


@pytest.mark.parametrize("number,expected_array", [
    (1, [1]),
    (10, [10]),
    (11, [10, 1]),
    (499, [400, 90, 9]),
    (400, [400]),
    (1234, [1000, 200, 30, 4])
])
def test_should_split_number_on_decimal_place_into_orders_of_ten(number, expected_array):
    assert split_number_into_orders_of_ten(number) == expected_array


@pytest.mark.parametrize("number, expected_order", [
    (1, 0),
    (10, 1),
    (100, 2),
    (1000, 3),
])
def test_should_return_calculate_order_of_ten(number, expected_order):
    assert calculate_order_of_ten(number) == expected_order
