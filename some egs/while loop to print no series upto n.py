num=int (input("enetr the value upto which the nos is to be printed => "))
i=1
linecount=1
while (i<=num):
    print(i,end='\t')
    if (linecount==10):
        print("\n")
        linecount=1
    linecount=linecount+1
    i=i+1
