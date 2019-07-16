cmake_minimum_required(VERSION 2.8.12)
project(simple_pybind_example LANGUAGES CXX C)
find_package(PythonInterp 3.7 REQUIRED)

set(CMAKE_CXX_STANDARD 14)
set(PYBIND11_PYTHON_VERSION 3.7 CACHE STRING "")

message("\n*** Dependencies:")
message("-- pybind11_DIR: " ${pybind11_DIR})
message("-- Python executable: " ${PYTHON_EXECUTABLE})
message("***\n")

set(ARTIFACTS_PATH ${CMAKE_SOURCE_DIR}/python_package/example_binding)

add_subdirectory(python_package/_cpp_package)
add_subdirectory(python_package/bindings)
