from math import sqrt
n= int (input("maximum number ->"))
for a in range (1,n+1):
        for b in range (a,n):
                c_square = a*2+b**2
                c=int (sqrt(c_square))
                if ((c_square - c**2)==0):
                      print (a,b,c)
                
