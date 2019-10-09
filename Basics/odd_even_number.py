n=int(input('enter the number of list '))
even=None
odd=None
number=[]
for i in range(0,n):
    number=int(input())
    
even=[n for n in number if n%2==0]
odd=[n for n in number if n%2!=0]
print(f"even={even} ,odd={odd}")
