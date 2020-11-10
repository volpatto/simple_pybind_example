#include <pybind11/pybind11.h>
#include <pybind11/functional.h>
#include "example_cpp.hpp"

namespace py = pybind11;

// This is a more complex python function wrapper, maybe unnecessary for most cases
auto py_function_wrapper(const py::function& f_python, double a, double b){
    auto f_wrapped = f_python.cast<std::function<double(double, double)>>();
    return example_cpp::f_multiply_wrapper(f_wrapped, a, b);
}

PYBIND11_MODULE(example_binding, m) {
    m.doc() = "pybind11 python_package plugin"; // optional module docstring

    m.def("add", (int (*) (int, int)) &example_cpp::add, "A function which adds two numbers", py::arg("i"), py::arg("j"));
    m.def("add", (double (*) (double, double)) &example_cpp::add, "A function which adds two numbers", py::arg("i"), py::arg("j"));

    m.def("f_multiply_wrapper", &example_cpp::f_multiply_wrapper);
//    m.def("f_multiply_wrapper", &py_function_wrapper);

}
