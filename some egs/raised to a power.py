x=int(input("Enter the no tobe raised => "))
p=int(input("enter the power to which no is to be raised => "))

pro=1
for i in range(1,p+1):
    pro=pro*x

print(x," raised to the power ",p ," is = ",pro)
