n=int (input("Enter a no"))
s=0
for i in range (1,n+1):
   s=s+(i**2)/i
   if (i==n):
       print(i**2,"/",i,end="")
   else : print(i**2,"/",i," + ",end="")

print(" = ", s)
