num=0
pnum=0
nnum=0
znum=0
while (num!= -1):
    num=int(input("Enter the no"))
    if (num>0):
        pnum+=1
    if (num<0):
        nnum+=1
    if (num==0):
        znum+=1

print("the no of positive nos are => ", pnum)
print("the no of negative nos are => ", nnum)
print("the no of zeroes are => ", znum)
    
