import large
a=int (input("Enetr the no => "))
b=int (input("Enetr the no => "))
x=large.compare (a,b)

print(dir(large))
if (x==a):
    print(a," is greater then ",b)
else :
     print(b," is greater then ",a)

