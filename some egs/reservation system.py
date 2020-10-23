travelling = input("ENter Yes or No")
i=1
while (travelling =='Yes'):
    num = input ("no of people travelling")
    for num in range(1,num+1):
        name = input("Name")
        age = input("Age")
        sex = input("Sex")
        print(name)
        print(age)
        print(sex)
    travelling= input('Oops you have forgot someone')
    
