#include<stdio.h>

//Factorial of a program using C recursive function

long long int fact(int n){
    if(n==0)
        return 1;
    else
        return (n*fact(n-1));
}

int main()
{
    int n;
    long long int f;
    printf("\nEnter number to find factorial of: ");
    scanf("%d",&n);

    if (n < 0)
        printf("Factorial of negative integers isn't defined.\n");
    else
      {
        f = fact(n);
        printf("%d! = %lld\n", n, f);
      }

    return 0;
}
