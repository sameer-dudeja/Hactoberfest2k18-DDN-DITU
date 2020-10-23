def cali(p,r,t):
    i=(p*r*t)/100
    return i


age =int (input("ENTER age =>"))
if (age>65):
    r=12
    p=int (input("ENTER principal amount =>"))
    t=int (input("ENTER time period in years =>"))
    i=cali(p,r,t)
    p=p+i
    print("The interest on the amount is => ", i)
    print("The total amount is => ", p)

else :
    r=10
    p=int (input("ENTER principal amount =>"))
    t=int (input("ENTER time period in years =>"))
    i=cali(p,r,t)
    p=p+i
    print("The interest on the amount is => ", i)
    print("The total amount is => ", p)
    
