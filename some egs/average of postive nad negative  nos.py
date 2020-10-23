num=0
pnum=0
nnum=0
znum=0
pavg=navg=0
pt=0
nt=0
while (num!= -1):
    num=int(input("Enter the no"))

    if (num>0):
        pt=pt+num
        pnum+=1
        
    elif (num<0):
        nt=nt+num
        nnum+=1
        
    elif (num==0):
        znum+=1



print(pt, nt)

print("the no of positive nos are => ", pnum)
print("the no of negative nos are => ", nnum)
print("the no of zeroes are => ", znum)

# average calculations

pavg=float (pt)/pnum
navg= float (nt)/nnum

print("the average of positive nos is => ", pavg)
print("the average of negative nos are => ", navg)
