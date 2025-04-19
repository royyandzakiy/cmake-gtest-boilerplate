# C++ Tests
add_executable(hello_tests
    test_main.cpp
    hello_test.cpp
)

target_link_libraries(hello_tests
    PRIVATE
    # hello_lib
    hello # this is called hello, from the hello_tests because ... (i still dont know)
    GTest::gtest # alternatively use GTest::gtest_main to not manually create main with ::testing::InitGoogleTest
)

include(GoogleTest)
gtest_discover_tests(hello_tests)

# Python Tests (pytest)
# find_package(Python COMPONENTS Interpreter Development REQUIRED)
# add_test(NAME python_tests
#     COMMAND ${Python_EXECUTABLE} -m pytest ${CMAKE_CURRENT_SOURCE_DIR}/python
#     WORKING_DIRECTORY ${CMAKE_BINARY_DIR}
# )