print("sum of the series of the type 1/1+2*2*2/2+3*3*3/3....")

no=int(input("\n Enter the value upto which sum is to be calculated => "))

i=1.0
sum=0.0
for i in range (1,no+1):
    sum=sum+((i**3)/i)
    if (i==no):
        print(i**3,'/',i,end ="")
        
    else: print(i**3,'/',i," + ",end ="")

print(" = " ,sum)
