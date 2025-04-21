import pytest
import os
# Removed CppFile and pytest_collect_file as they are not needed
# for standard pytest-cpp discovery based on testpaths and cpp_files.

def pytest_addoption(parser):
    """Adds command line options for pytest."""
    parser.addoption(
        "--cpp-executable",
        action="store",
        # Set the default path to the likely location of the compiled executable
        # based on your build structure (Windows, Debug config).
        # You might need to adjust this path if you use different build
        # configurations (e.g., Release) or operating systems.
        # default="build/tests/Debug/hello_tests.exe",
        help="Path to C++ test executable"
    )
