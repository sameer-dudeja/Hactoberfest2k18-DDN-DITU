import math
def cal(endterm):
    i=j=a=b=sum=0
    for i in range(1,endterm):
        sum=sum+(i**i/i)
        print("sum of the seies is => ", sum)

endterm=int (input("The term upto which the term is to becalculated is => "))
cal (endterm)
