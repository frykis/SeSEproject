import pytest
import numpy as np
from example import ffi, lib


def cast_matrix(matrix, ffi):
	ap = ffi.new("double* [%d]" % (matrix.shape[0]))
	ptr = ffi.cast("double *", matrix.ctypes.data)
	for i in range(matrix.shape[0]):
		print i*matrix.shape[1]
		ap[i] = ptr + i*matrix.shape[1]                                                                
	return ap 

def test_example_FFT():
	"""
	Test FFT of 
	"""
	
	assert lib.example_FFT_ones(4) == 4.0



def test_example_FFT_manipulate_list():
	"""
	Test FFT of 
	"""
	NUM_POINTS = 4
	coeff = [1.0]*NUM_POINTS
	temp = ffi.new("double []", coeff)
	lib.example_FFT_manipulate_list(temp)
	newList = [1.0]*NUM_POINTS
	for i in range(NUM_POINTS):
		newList[i] = temp[i]
	coeff[0] = 2
	assert newList == coeff



def example_FFT_struct():
	"""
	Test FFT of 
	"""
	#p = ffi.new("foo_t *", [5, [6, 7, 8]]) # length 3

	p = ffi.new("double [][]", [[5],[5]])         # length 3 with 0 in the array
	#p = ffi.new("foo_t *", {'y': 3})       # length 3 with 0 everywhere




# def test_example_FFT_signal():
# 	"""
# 	Test FFT of 
# 	"""
# 	NUM_POINTS = 4
# 	coeff = [1.0]*NUM_POINTS
# 	assert lib.example_FFT_signal(NUM_POINTS, coeff) == [1, 1, 1, 1]



if __name__ == '__main__':
	#example_FFT_signal()
	#example_FFT_struct()
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
	print 'numpy says', m.sum()

	m_p = cast_matrix(m, ffi)

	sm = C.sum(m_p, m.shape[0], m.shape[1])
	print 'cffi says', sm



