import pytest
from example import ffi, lib


def test_example_FFT():
    """
    Test printing.
    """
    
    assert lib.example_FFT(4) == 4.0


def test_Hello_World():
    """
    Test printing.
    """
    temp = lib.example_Hello();

    print temp
    assert lib.example_Hello() == 0
