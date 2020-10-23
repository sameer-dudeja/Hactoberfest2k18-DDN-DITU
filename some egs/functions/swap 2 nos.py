def swap (a,b):
    a=a+b
    b=a-b
    a=a-b
    print ("Swapped nos are :- a = "+str(a)+" b = "+ str(b))

a=int (input("Enter a no => "))
b=int (input("Enter a no => "))
swap (a,b)
