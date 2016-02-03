#include <rfftw.h>
#include <math.h>

#define NUM_POINTS 64
#define REAL 0
#define IMAG 1

void generate_signal(fftw_real* signal) {
	int i;
	for (i = 0; i <NUM_POINTS; i++) {
		double theta = (double)i / NUM_POINTS * M_PI;
		signal[i] = 1.0 * cos(10.0 * theta) +
					0.5 * cos(25.0 * theta);
	}
}

void compute_magnitude(fftw_real* result) {
	int i;
	for (i = 0; i < NUM_POINTS; i++) {
		double mag = sqrt(result[i][REAL] * result[i][REAL] + 
						  result[i][IMAG] * result[i][IMAG]);
		printf("%g\n",mag);
	}
}

int main() {
	fftw_real signal[NUM_POINTS];
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