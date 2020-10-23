num=int(input("enter the binary no"))
num1=num
i=0
no=0
n=0
while(num!=0):
   n=num%10
   no=no+n*(2**i)
   num=num//10
   i+=1

print("the value of the binary no in decimal is ", no)
