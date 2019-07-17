import pytest

from python_package.foo_module import add_wrapper


@pytest.mark.parametrize("num_1, num_2, expected_type", [
    [1, 1, int],
    [1., 1, float],
    [1, 1., float],
    [1., 1., float]
])
def test_add_wrapper_type_results(num_1, num_2, expected_type):
    assert type(add_wrapper(num_1, num_2)) == expected_type


@pytest.mark.parametrize("num_1, num_2, expected_result", [
    [1, 2, 3],
    [0., 1, 1.],
    [0, 0., 0.],
    [-1., 2, 1.]
])
def test_add_wrapper_operation(num_1, num_2, expected_result):
    assert add_wrapper(num_1, num_2) == pytest.approx(expected_result)
