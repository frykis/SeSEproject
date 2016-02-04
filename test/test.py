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
    temp2 = ffi.new("double []", [1,1,1,1])
    print temp2[0]
    temp = ffi.new("double []", 4)
    lib.example_FFT_signal(temp2)

    print temp2[0]


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



