cmake_minimum_required(VERSION 2.8.12)
project(simple_pybind_example LANGUAGES CXX)
set(CMAKE_CXX_COMPILER gcc)

set(CMAKE_CXX_STANDARD 14)

add_subdirectory(python_package/_cpp_package)
#target_link_libraries(example)
add_subdirectory(python_package/bindings)
include_directories("${PROJECT_BINARY_DIR}")
