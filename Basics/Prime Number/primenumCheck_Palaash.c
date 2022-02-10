#include <stdio.h>

//Simple C program to check whether a number is prime or not using recursion

int checkPrime(int n, int i){
  if(i==1){
      return 1;
  }
  
  else
  {
      
      if (n%i==0) {
          return 0;
      }
      else {
          return checkPrime(n,i-1);
      }
      
  }
  

}

int main()
{
   int num, check;
    printf("Enter a number: ");
    scanf("%d", &num);
    check = checkPrime(num, num / 2);
    if (check == 1)
    {
        printf("%d is a prime number\n", num);
    }
    else
    {
        printf("%d is not a prime number\n", num);
    }
    return 0;
}