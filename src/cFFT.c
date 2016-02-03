#include <fftw3.h>
#include <math.h>
#include <stdio.h>

#define NUM_POINTS 64 //Power of two.
#define REAL 0
#define IMAG 1

void generate_signal(fftw_complex* signal) {
	int i;
	for (i = 0; i <NUM_POINTS; i++) {
		double theta = (double)i / NUM_POINTS * M_PI;
		signal[i][REAL] = 1.0 * cos(10.0 * theta) +
					0.5 * cos(25.0 * theta);
		signal[i][IMAG] = 0.0;		
		printf("%g\n",signal[i][REAL]);	
	}
}

void compute_magnitude(fftw_complex* result) {
	int i;
	for (i = 0; i < NUM_POINTS; i++) {
		double mag = sqrt(result[i][REAL] * result[i][REAL] + 
						  result[i][IMAG] * result[i][IMAG]);
		printf("%g\n",mag);
	}
}

int main() {
	fftw_complex signal[NUM_POINTS];
	fftw_complex result[NUM_POINTS];

	fftw_plan plan = fftw_plan_dft_1d(NUM_POINTS,
									  signal,
									  result,
									  FFTW_FORWARD,
									  FFTW_ESTIMATE);

	generate_signal(signal);
	fftw_execute(plan);
	compute_magnitude(result);

	fftw_destroy_plan(plan);

	return 0;
}