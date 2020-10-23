print("sum of series of type 1/1+1/2+1/3+1/4+1/5+...........")
no=int(input("\n Enter the value upto which sum is to be calculated => "))

i=1
sum=0.0
for i in range (1,no+1):
    sum=sum+(1/i)
    if (i==no):
        print(1,'/',i,end ="")
        
    else: print(1,'/',i," + ",end ="")

print(" = " ,sum)
