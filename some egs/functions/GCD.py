def GCD (x,y):
    rem=x%y
    if (rem==0):
        print (x ," ", y)
        return y
    else :
        return GCD(y,rem)

a1 = int (input("the first no => "))
a2 = int (input("the Second no => "))
print("the GCD of the nos ",a1," and ", a2, "is => ", GCD(a1,a2))
