def fibo(n):
    sum=0
    j=1
    i=0
    
    for k in range (1,n+1):        
        print(sum,end=" ")
        i=j;
        j=sum
        sum=i+j

x=int (input("Enter the no upto which the fibinacci seereis is to be calculated => "))
fibo(x)
