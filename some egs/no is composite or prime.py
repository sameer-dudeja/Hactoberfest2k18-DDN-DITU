no=int(input("Enter a n to check => "))
n=no
i=1
iscomp=0
for i in range(2,no):
    if (no%i==0):
        iscomp=1
        break
    else : i=i+1

if (iscomp==1):
    print(n," is a composite no")
elif(iscomp==0):
    print(n," is a prime no")
