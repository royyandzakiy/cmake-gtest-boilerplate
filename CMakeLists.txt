cmake_minimum_required(VERSION 3.15)
project(HelloWorld LANGUAGES CXX)

# Set C++17 standard
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

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

# Enable coverage for GCC/MinGW
if(CMAKE_CXX_COMPILER_ID MATCHES "GNU|Clang")
    add_compile_options(-fprofile-arcs -ftest-coverage)
    add_link_options(--coverage)
endif()

# ------------- Testing Directories ------------- 
# Add subprojects
add_subdirectory(hello)
add_subdirectory(app)
add_subdirectory(tests)