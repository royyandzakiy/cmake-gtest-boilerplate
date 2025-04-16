cmake_minimum_required(VERSION 3.15)
project(HelloWorld LANGUAGES CXX)

# Set C++17 standard
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Add main library and executable
add_library(hello_lib src/hello.cpp src/hello.h)
add_executable(hello_world src/main.cpp)
target_link_libraries(hello_world PRIVATE hello_lib)

# Download and configure GoogleTest
include(FetchContent)
FetchContent_Declare(
  googletest
  GIT_REPOSITORY https://github.com/google/googletest.git
  GIT_TAG release-1.12.1  # Latest stable as of 2023
)
FetchContent_MakeAvailable(googletest)

# Enable testing
enable_testing()

# Add tests subdirectory
add_subdirectory(tests)