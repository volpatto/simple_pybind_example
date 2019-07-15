//
// Created by volps on 15/07/19.
//

#include <pybind11/pybind11.h>
#include "example_cpp.hpp"

namespace py = pybind11;

PYBIND11_MODULE(example_cpp, m) {
m.doc() = "pybind11 python_package plugin"; // optional module docstring

m.def("add", &add, "A function which adds two numbers");
}
