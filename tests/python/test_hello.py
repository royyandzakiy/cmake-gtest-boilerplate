import ctypes
import os
import pytest

# Load the compiled library
lib = ctypes.CDLL(os.path.join(os.path.dirname(__file__), '../../build/hello/libhello.so'))

def test_hello_world():
    lib.hello_world.restype = ctypes.c_char_p
    result = lib.hello_world()
    assert result.decode('utf-8') == "Hello, World!"