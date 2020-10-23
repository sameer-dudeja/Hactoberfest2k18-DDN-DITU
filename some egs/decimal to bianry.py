num=int(input("Enter the no"))
i=0
n=0
num1=num
binarynum=0
while (num!=0):
    n=num%2
    binarynum = binarynum + n*(10**i)
    num//=2
    i+=1

print("the binary no of ",num1," is ", binarynum)
