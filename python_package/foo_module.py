from python_package.cpp_binding.example_binding import add, f_multiply_wrapper


def add_wrapper(a, b):
    return add(a, b)


def f_wrapper(func, a, b):
    return f_multiply_wrapper(func, a, b)
