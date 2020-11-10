#include "example_cpp.hpp"

namespace example_cpp {

    int add(int i, int j)
    {
        return i + j;
    }

    double add(double i, double j)
    {
        return i + j;
    }

    double f_multiply_wrapper(const std::function<double(double, double)>& f, double a, double b) {
        return f(a, b);
    }

}
