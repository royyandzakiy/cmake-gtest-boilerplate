cmake_minimum_required(VERSION 3.15)
project(HelloWorld LANGUAGES CXX)

# Set C++17 standard
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# ------------- Library & Executable Directories ------------- 
# Add main library and executable
add_library(hello_lib src/hello.cpp src/hello.h)      # create libraries here from different .h and .cpp
add_executable(hello_world src/main.cpp)              # main executable
target_link_libraries(hello_world PRIVATE hello_lib)  # link the main to the different libraries

# ------------- Testing Setup ------------- 
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

# ------------- Testing Directories ------------- 
# Add tests subdirectory
add_subdirectory(tests)