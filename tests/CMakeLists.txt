add_executable(hello_tests
    test_main.cpp
    hello_test.cpp
)

target_link_libraries(hello_tests
    PRIVATE
    hello_lib
    GTest::gtest # alternatively use GTest::gtest_main to not manually create main with ::testing::InitGoogleTest
)

include(GoogleTest)
gtest_discover_tests(hello_tests)