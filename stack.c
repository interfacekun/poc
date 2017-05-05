#include <stdio.h>
#include  <stdlib.h>

void why_it_tun(void){
	printf("why run here ?!\n");
	exit(0);
}

void we_call(void){
	int buff[2];

	buff[0] = 0;
	buff[1] = 1;
	buff[3] = (int)why_it_tun;
}

int main(void){
	we_call();

	return  0;
}