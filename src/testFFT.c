#include <fftw3.h>
#include <math.h>
#include <stdio.h>

#define NUM_POINTS 4
#define REAL 0
#define IMAG 1

void generate_signal(fftw_complex* signal) {
	int i;
	for (i = 0; i <NUM_POINTS; i++)
		signal[i][REAL] = 1;
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