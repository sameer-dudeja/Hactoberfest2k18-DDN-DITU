m=int(input("Enter the value of m => "))
n=int(input("Enter the value of n (greater than m)"))
i=m
for i in range(m,n+1):
    if (m%2==0):
        print(i ," is even")
    elif (m%2!=0):
        print(i ," is odd")
    i=i+1
