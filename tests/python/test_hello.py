import os
import ctypes
import pytest

def test_hello_function():
    base_path = os.path.join(os.path.dirname(__file__), '../../build/hello/Debug') # Added '/Debug' here
    lib_name = 'hello.dll'
    lib_path = os.path.join(base_path, lib_name)

    if not os.path.exists(lib_path):
        lib_name_with_lib = 'libhello.dll'
        lib_path_with_lib = os.path.join(base_path, lib_name_with_lib)
        if os.path.exists(lib_path_with_lib):
            lib_path = lib_path_with_lib
        else:
            raise FileNotFoundError(f"Could not find the shared library at: {lib_path} or {lib_path_with_lib}")

    lib = ctypes.CDLL(lib_path)
    lib.hello.restype = ctypes.c_char_p
    result = lib.hello()
    assert result.decode('utf-8') == "Hello from C++!"

if __name__ == "__main__":
    test_hello_function()