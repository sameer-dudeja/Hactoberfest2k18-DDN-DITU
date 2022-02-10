#include<stdio.h>
#include<conio.h>
int fibonacci(int n)
{
	if(n==0)
		return 0;
	else if(n==1)
		return 1;
	else	
		return (fibonacci(n-1)+fibonacci(n-2));
}

void main()
{
	clrscr();
	int val,i;
	printf("Enter the value:");
	scanf("%d",&val);
	printf("Fibonacci series of %d is ",val);
	for(i=0;i<=val;i++)
		printf("%d\t",fibonacci(i));
	getch();
}
