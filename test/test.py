import pytest
import numpy as np
from example import ffi, lib

def c2pyList(ptr,NUM_POINTS):
        """
        Transform list from double* to a Python list.
        """
        pyList = [1.0]*NUM_POINTS
        for i in range(NUM_POINTS):
                pyList[i] = ptr[i]
        return pyList


def c2pyMatrix(ptr_ptr, NUM_POINTS): #Only for lists [NUM_POINTS][2]
        """
        Transform array from double** to a Python array.
        """
        pyMatrix = [[0 for x in range(2)] for x in range(NUM_POINTS)]
        for ii in range(NUM_POINTS):
                pyMatrix[ii][0] =  ptr_ptr[ii][0]
                pyMatrix[ii][1] =  ptr_ptr[ii][1]
        return pyMatrix


def cast_matrix(matrix, ffi):
        """
        Transform array into a double** which can be passed to a c-function.
        """
        ptr_ptr = ffi.new("double* [%d]" % (matrix.shape[0])) # List of pointers
        ptr = ffi.cast("double*", matrix.ctypes.data) # Pointer to data set
        for i in range(matrix.shape[0]):
                ptr_ptr[i] = ptr + i*matrix.shape[1]
        return ptr_ptr

# radovan: this throws errors, took it out for the moment
def deactivated_test_sum_example():
        """
        Test: Create a C-function in Python via FFI. Pass argument to function and validate result with Numpy.
        """

        ffi.cdef("""
                double sum(double**, int, int);
                """)
        C = ffi.verify("""
                double sum(double** matrix,int x, int y){
                int i, j;
                double sum = 0.0;
                for (i=0; i<x; i++){
                        for (j=0; j<y; j++){
                                sum = sum + matrix[i][j];
                        }
                }
        return(sum);
        }
        """)
        m = np.ones(shape=(10,10))

        m_p = cast_matrix(m, ffi)

        sm = C.sum(m_p, m.shape[0], m.shape[1])

        assert m.sum() == sm



def test_example_FFTM_manipulate_int():
        """
        Test: argument gives length of array of complex numbers that is created in C-code. The complex numbers are all 1 + i*0.
                  The function example_FFT_ones(int) returns the first fourier coefficient generated from this array. Should be equal to the argument.
        """

        assert lib.example_FFT_ones(4) == 4.0


def test_example_FFT_manipulate_list():
        """
        Test: Send a list of integers to a c-function. Manipulate the first element and return. Check that this is done correctly.
        """
        NUM_POINTS = 4
        coeff = [1.0]*NUM_POINTS
        temp = ffi.new("double []", coeff)
        lib.example_FFT_manipulate_list(temp)
        newList = c2pyList(temp,NUM_POINTS)
        coeff[0] = 2
        assert newList == coeff



def test_example_FFT_manipulate_matrix():
        """
        Test: Send a matrix of doubles to a c-function. This is done by passing a double**. Manipulate the first element ([0][0]) and return. Check that this is done correctly.
        """
        NUM_POINTS = 4
        m = np.ones(shape=(NUM_POINTS,2))
        m_p = cast_matrix(m,ffi)

        lib.example_FFT_manipulate_matrix(m_p)
        newMatrix = c2pyMatrix(m_p,NUM_POINTS)
        m[0][0] = 2.0

        assert (newMatrix == m).all()


def test_example_FFT_signal():
        """
        Test: Compute fourier coefficients of array with complex data.
    """
        NUM_POINTS = 4
        m = np.ones(shape=(NUM_POINTS,2))
        m[:,1] = 0
        m_p = cast_matrix(m,ffi)
        lib.example_FFT_signal(NUM_POINTS, m_p)
        newMatrix = c2pyMatrix(m_p,NUM_POINTS)
        mag = [0.0]*NUM_POINTS
        for i in range(NUM_POINTS):
                mag[i] = np.sqrt(newMatrix[i][0]*newMatrix[i][0] +
                                             newMatrix[i][1]*newMatrix[i][1])
        assert mag == [4.0,0.0,0.0,0.0]
