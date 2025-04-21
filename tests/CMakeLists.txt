# C++ Tests
add_executable(hello_test
    hello_test.cpp
)

target_link_libraries(hello_test
    PRIVATE
    hello # this is called hello, from the hello_tests because ... (i still dont know)
    GTest::gtest_main # alternatively use GTest::gtest, but need to manually create main with ::testing::InitGoogleTest
)

include(GoogleTest)
gtest_discover_tests(hello_test)