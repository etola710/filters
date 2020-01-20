#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int main()
{
	float dt = 0.5;
	float xk_1 = 0, vk_1 = 0, a = 0.85, b = 0.005;
	float xk, vk, rk;
	float xm;
	int time = 0;
	while(1)
	{
		// input signal
		xm = rand() % 100;
		xk = xk_1 + ( vk_1 * dt );
		vk = vk_1;
		rk = xm - xk;
		xk += a * rk;
		vk += ( b * rk ) / dt;
		xk_1 = xk;
		vk_1 = vk;
		// printf("%f \t %f\n", xm, xk_1);
		FILE *gnuplotPipe = popen("gnuplot","w");
		fprintf(gnuplotPipe,"plot '-'\n");
		fprintf(gnuplotPipe, "%d %f\n",time,xm);
		time++;
		sleep(1);
	}
}
