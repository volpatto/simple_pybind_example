cmake_minimum_required(VERSION 2.8.12)
project(simple_pybind_example LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 14)
set(CMAKE_MODULE_PATH /home/diego/Work/miniconda/envs/cpp-bindings/bin/cmake)

include_directories(example)
find_package(pybind11)

add_executable(simple_pybind_example
        example/example.cpp)

pybind11_add_module(example example/example.cpp)
