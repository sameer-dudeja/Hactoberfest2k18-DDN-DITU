a = float(input("enter the length of first side"))
b = float(input("Enter the length of second side"))
c = float(input("Enter the length of third side"))

s=(a+b+c)/2

area=(s*(s-a)*(s-b)*(s-c))**0.5
print(a,b,c)
print("area of the triangle using heron's formula for triangle whose sides is " + str(a)+"  " + str(b)+"   "+ str(c) +"  is  : - " , format(area,"0.2f") ,)
