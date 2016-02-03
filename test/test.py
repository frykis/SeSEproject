import pytest
from example import ffi, lib





def test_Hello_World():
    """
    Test printing.
    """
    temp = lib.example_Hello();

    print temp
    assert lib.example_Hello() == 0
