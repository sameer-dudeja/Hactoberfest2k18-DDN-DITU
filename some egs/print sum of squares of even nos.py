n= int (input("Enter the value upto which squares are to be found"))
i=0
sum=0.0
for i in range (2,n+1,2):
    sum=sum+(i**2)
    if (i==n):
        print(i**2,end="")
    else : print(i**2,"+",end="")

print(" = ", sum)
