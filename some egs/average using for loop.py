n=int (input("enter the no upto which average is to be found => "))
i=0
sum=0.0
for i in range(n+1):
    sum=sum+i

average=sum/n
print("the sum of the nos upto ",n," is => ",sum)
print("the average of nos upto ",n," is => ", average)
