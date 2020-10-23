lin=int(input("enter the no of lines"))
i=j=0
for i in range(lin+1):
    for k in range (lin,i,-1):
        print(" ",end=' ')
    for j in range (1,i+1):
        print(j, end=" ")
    for l in range (i-1,0,-1):
        print(l,end=" ")
    print("\n")
