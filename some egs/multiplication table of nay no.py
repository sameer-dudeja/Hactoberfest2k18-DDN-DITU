no=int(input("enter the multiplicand => "))
lim=int (input("enter the limit upto which no is to be multiplied => "))
i=0
pro=0
for i in range(lim+1):
    pro=no*i
    print (no," * ", i ," = ",pro)
