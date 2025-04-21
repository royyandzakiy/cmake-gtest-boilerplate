cmake_minimum_required(VERSION 3.15)
project(hello LANGUAGES CXX)

# # Enable code coverage
# if(CMAKE_CXX_COMPILER_ID STREQUAL "GNU" OR CMAKE_CXX_COMPILER_ID STREQUAL "Clang")
#     add_compile_options(-fprofile-arcs -ftest-coverage)
#     add_link_options(--coverage)
# endif()

# Enable coverage for GCC/MinGW (even when using MSVC)
if(CMAKE_CXX_COMPILER_ID MATCHES "GNU|Clang" OR WIN32)
    add_compile_options(--coverage)
    add_link_options(--coverage)
endif()

add_library(hello
    src/hello.cpp
    include/hello.h
)

target_include_directories(hello PUBLIC 
    $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include>
    $<INSTALL_INTERFACE:include>
)

# Install targets
install(TARGETS hello
    ARCHIVE DESTINATION lib
    LIBRARY DESTINATION lib
    RUNTIME DESTINATION bin
)

install(DIRECTORY include/ DESTINATION include)