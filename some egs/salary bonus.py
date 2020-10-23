sal= int (input("Enetr the salary of the employee => "))
gen=input("Enter the gender of teh employee (male -> m/M and female ->f/F) =>")

if (sal<=10000 and gen=='M'or gen=='m'):
      bonus=sal*0.05+0.02*sal
      sal=sal+bonus
      print("the bonus earned on DIWALI by the employee is ", bonus)
      print("the salary of the employee is ", sal)

elif (sal<=10000 and gen=='F'or gen=='f'):
      bonus=sal*0.1+0.02*sal
      sal=sal+bonus
      print("the bonus earned on DIWALI by the employee is ", bonus)
      print("the salary of the employee is ", sal)
      
elif (gen=='M'or gen=='m'):
      bonus=sal*0.05
      sal=sal+bonus
      print("the bonus earned on DIWALI by the employee is ", bonus)
      print("the salary of the employee is ", sal)

elif (gen=='F'or gen=='f'):
      bonus=sal*0.1
      sal=sal+bonus
      print("the bonus earned on DIWALI by the employee is ", bonus)
      print("the salary of the employee is ", sal)

