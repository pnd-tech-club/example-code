#include <stdio.h>

int main()
{
	char usrname[20];
	int a, b;
	int c;

	printf("\nWhat's your name?: ");
	scanf("%19s", &usrname);
	printf("\nWhy hello, %s!", usrname);
	
	a = 2;
	b = 2;
	c = a + b;
	printf("\n2 plus 2 is: %d\n", c);

	return(0);
}
