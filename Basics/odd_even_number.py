number[]=input('enter the list ')
even=None
odd=None
even=[n for n in number if n%2==0]
odd=[n for n in number if n%2!=0]
print(f"even={even} ,odd={odd}")
