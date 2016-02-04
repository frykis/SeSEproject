import pytest
from example import ffi, lib

def transform_ones():
    NUM_POINTS = 4
    value = lib.example_FFT(NUM_POINTS)
    print value


if __name__ == '__main__':
	transform_ones();