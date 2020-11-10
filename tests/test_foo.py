import pytest

from python_package.foo_module import add_wrapper, f_wrapper


def multiply(a, b):
    return a * b


def add(a, b):
    return a + b


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


@pytest.mark.parametrize("func, a, b, expected_result", [
    [add, 1, 1, 2],
    [add, -1, 1, 0],
    [multiply, 1, 2, 2],
    [multiply, 2, 3, 6],
    [multiply, -5, 5, -25]
])
def test_function_wrapper(func, a, b, expected_result):
    wrapper_result = f_wrapper(func, a, b)
    assert wrapper_result == expected_result
