lin=int(input("enter the no of lines"))
i=j=0
for i in range(lin+1):
    for k in range (lin,i,-1):
        print(" ",end=' ')
    for j in range (1,i+1):
        print(i, end=" ")
    print("\n")
