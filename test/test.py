import pytest
from example import ffi, lib


def test_example_FFT():
    """
    Test FFT of 
    """
    
    assert lib.example_FFT(4) == 4.0




def example_FFT_signal():
    """
    Test FFT of 
    """
    NUM_POINTS = 4
    coeff = [1.0]*NUM_POINTS
    temp = lib.example_FFT_signal(NUM_POINTS, coeff)
    print temp[1]


def test_example_FFT_signal():
    """
    Test FFT of 
    """
    NUM_POINTS = 4
    coeff = [1.0]*NUM_POINTS
    assert lib.example_FFT_signal(NUM_POINTS, coeff) == [1, 1, 1, 1]


def test_Hello_World():
    """
    Test printing.
    """
    temp = lib.example_Hello();

    print temp
    assert lib.example_Hello() == 0


if __name__ == '__main__':
	example_FFT_signal()



