find_package(pybind11 REQUIRED)

# Generate Python module with pybind11
add_subdirectory(third_party/pybind11)
pybind11_add_module(
        example_binding
            bindings.cpp
)

target_link_libraries(
        example_binding
        PRIVATE
            example
)
