n= int (input("Enter the value upto which cobes are to be found"))
i=0
sum=0.0
for i in range (1,n+1):
    sum=sum+(i**3)
    if (i==n):
        print(i**3," + ",end="")
    else:print(i**3,"+",end="")

print(" = ", sum)
