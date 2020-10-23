ch='a'
uch=0
lch=0
d=0
s=0
while (ch!='*'):
    ch = input("enter the character (enter '*' to end) =>")
    if (ch.isalpha()):
        if (ch.isupper()):
            uch+=1
            
        elif(ch.islower()):
            lch+=1

    elif (ch.isdigit()):
        d+=1
    else : s+=1

print("the no of upper case letters are", uch)
print("the no of lower case letters are", lch)
print("the no of digits are", d)
print("the no of special case letters are", s)
