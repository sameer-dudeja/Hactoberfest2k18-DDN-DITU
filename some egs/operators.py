#assignment operators

a=5
a+=5
print(a)

a**=5
print(a)

# comparison operator

val=10
num=20
compare = val==num
print(compare)

if val==num:
    print(' equal')
elif val>num:
    print("greater")
elif val<num:
    print('smaller')
if val!=num:
    print("not equal")

#logical oprators

x=10
if x>10 or x>5:
    print (x)

# identity operators
list1 =['banana',20,30]
list2=[10,20,30]

x=list1
x is list1
print (x is not list1)

list1 is list2
print(list1 is not list2)


# membership operators

x in list1

print( 10 in list1)
print(10 in list1)
    
#BITWISE OPERATOR
print(10&12)
print(10|12)


