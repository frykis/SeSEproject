#include <fftw3.h>
#include <math.h>
#include <stdio.h>
#include <example.h>

#define REAL 0
#define IMAG 1

void generate_signal_ones(fftw_complex* signal, int NUM_POINTS) {
	int i;
	for (i = 0; i <NUM_POINTS; i++)
		signal[i][REAL] = 1;
}

void generate_signal(fftw_complex* signal,double** coeff, int NUM_POINTS) {
	int i;
	for (i = 0; i <NUM_POINTS; i++) {
		signal[i][REAL] = coeff[i][REAL];
		signal[i][IMAG] = coeff[i][IMAG];
	}
}

void generate_python_output(fftw_complex* result, double** coeff, int NUM_POINTS) {
	int i;
	for (i = 0; i <NUM_POINTS; i++) {
		coeff[i][REAL] = result[i][REAL];
		coeff[i][IMAG] = result[i][IMAG];
	}
}

void compute_magnitude(fftw_complex* result, int NUM_POINTS) {
	int i;
	for (i = 0; i < NUM_POINTS; i++) {
		double mag = sqrt(result[i][REAL] * result[i][REAL] + 
						  result[i][IMAG] * result[i][IMAG]);
		printf("%g\n",mag);
	}
}

double example_FFT_ones(int NUM_POINTS) {
	fftw_complex signal[NUM_POINTS];
	fftw_complex result[NUM_POINTS];

	fftw_plan plan = fftw_plan_dft_1d(NUM_POINTS,
									  signal,
									  result,
									  FFTW_FORWARD,
									  FFTW_ESTIMATE);

	generate_signal_ones(signal, NUM_POINTS);
	fftw_execute(plan);

	fftw_destroy_plan(plan);

	return result[0][REAL];
}


void example_FFT_manipulate_list(double coeff[]) {
	coeff[0] = 2;
}

void example_FFT_manipulate_matrix(double** coeff) {
	coeff[0][0] = 2;
}



void example_FFT_signal(int NUM_POINTS, double** coeff) {
	fftw_complex signal[NUM_POINTS];
	fftw_complex result[NUM_POINTS];

	fftw_plan plan = fftw_plan_dft_1d(NUM_POINTS,
									  signal,
									  result,
									  FFTW_FORWARD,
									  FFTW_ESTIMATE);

	generate_signal(signal, coeff, NUM_POINTS);
	fftw_execute(plan);
	generate_python_output( result, coeff, NUM_POINTS);
	
	
	fftw_destroy_plan(plan);
}

	

