num=int (input("Enter a no to check for avogardos no => "))
num1=num
s=0
temp=0
while (num>0):
    temp=num%10
    s+=(temp**3)
    num//=10
print(s)
if (s==num1):
    print("the value enetred by you is an avogadros no")

else : print ("the value enetred by you is not an avogadros no")
