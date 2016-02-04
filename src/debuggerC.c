#include <stdio.h>
#include <fftw3.h>
#include <math.h>
#include "debugger.h"


int main(int argc, char const *argv[])
{
	printf("%g\n",example_FFT(4));
	return 0;
}