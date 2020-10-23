# %%%%%%
# ^^^^^^
# ^^^^^^^^^^
# ^^^^^^^^^^

def  p (c="%",n=6,r=1):
    for i in range (r):
        print()
        for j in range (n):
            print(c,end=" ")


c=input("character => ")
n=int(input("no of times "))
r=int(input("no of rows => "))

p()
p(c)
p(c,n,r)
