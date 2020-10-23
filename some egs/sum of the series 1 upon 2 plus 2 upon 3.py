print("the sum of the series 1/2+2/3+3/4......... ")
no=int(input("\n Enter the value upto which sum is to be calculated => "))

i=1
sum=0.0
for i in range (1,no+1):
    sum=sum+(i/i+1)
    if (i==no):
        print(i,'/',i+1,end ="")
        
    else: print(i,'/',i+1," + ",end ="")

print(" = " ,sum)
