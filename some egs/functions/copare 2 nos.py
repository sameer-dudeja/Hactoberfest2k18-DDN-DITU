def compare(a,b):
    if (a==b):
        print(str(a)+ " and "+str(b) +" are equal ")
    else:
        print (str(a)+ " and "+str(b) +" are not equal ")
        if (a>b):
            print (str(a)+ " is greater than "+str(b))
        else:
            print (str(b)+ " is greater than "+str(a))


        
a=int (input("ENTER a no =>"))
b=int (input("ENTER a no =>"))
compare(a,b)
