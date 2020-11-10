#include <functional>

namespace example_cpp {

    int add(int i, int j);

    double add(double i, double j);

    double f_multiply_wrapper(const std::function<double(double, double)>& f, double a, double b);

}