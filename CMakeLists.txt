cmake_minimum_required(VERSION 2.8.12)
project(simple_pybind_example)

set(CMAKE_CXX_STANDARD 14)

# Set source directory
set(SOURCE_DIR "${CMAKE_CURRENT_SOURCE_DIR}/python_package/cpp_package")

# Tell CMake that headers are also in SOURCE_DIR
include_directories(${SOURCE_DIR})

set(SOURCES "${SOURCE_DIR}/example_cpp.cpp")

# Generate Python module with pybind11
add_subdirectory(third_party/pybind11)
pybind11_add_module(cpp_example ${SOURCES} "${SOURCE_DIR}/bindings.cpp")
