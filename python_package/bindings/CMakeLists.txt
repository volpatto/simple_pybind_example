find_package(pybind11 REQUIRED)
set(pybind11_DIR python_package/bindings/third_party/pybind11/tools)
include(pybind11Tools)

include_directories("${PROJECT_BINARY_DIR}/python_package/_cpp_package")

# Generate Python module with pybind11
#add_subdirectory(${CMAKE_CURRENT_SOURCE_DIR}/third_party/pybind11)
pybind11_add_module(
        example_binding
            bindings.cpp
)
target_link_libraries(example)
target_link_libraries(
        example_binding
        PRIVATE
            example
)
