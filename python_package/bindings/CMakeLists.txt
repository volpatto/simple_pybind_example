find_package(pybind11 REQUIRED)

include_directories("${PROJECT_SOURCE_DIR}/python_package/_cpp_package")

# Generate Python module with pybind11
pybind11_add_module(
        example_binding
            bindings.cpp
)

target_link_libraries(
        example_binding
        PRIVATE
            example
)

install(
        TARGETS example_binding
        RUNTIME DESTINATION ${ARTIFACTS_PATH}
        LIBRARY DESTINATION ${ARTIFACTS_PATH}
        ARCHIVE DESTINATION ${ARTIFACTS_PATH}
)