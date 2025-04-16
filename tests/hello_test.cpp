#include <gtest/gtest.h>
#include "../src/hello.h"

TEST(HelloTest, OutputCheck) {
    EXPECT_EQ(hello_world(), "Hello, World from C++17!");
}

TEST(HelloTest, NonEmptyOutput) {
    EXPECT_FALSE(hello_world().empty());
}