from python_package.cpp_binding.example import add


def hello():
    print("Hi, there. Let's do some crazy cpp bindings!")


def add_wrapper(a, b):
    return add(a, b)
