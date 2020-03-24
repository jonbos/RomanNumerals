import pytest


@pytest.mark.parametrize("truthy_args", [1, 1.0, True])
def test_smoke_test(truthy_args):
    assert truthy_args == True
