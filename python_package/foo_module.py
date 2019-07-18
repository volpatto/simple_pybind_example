from python_package.cpp_binding.example_binding import add


def add_wrapper(a, b):
    return add(a, b)
