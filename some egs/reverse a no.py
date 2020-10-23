no=int(input("Enter the no => "))
num1=0
num=no
print("the reverse of the no is")
while (num>0):
    num1=num%10
    print(num1,end="")
    num=num//10


