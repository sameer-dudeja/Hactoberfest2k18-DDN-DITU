age = int (input("Enter the age of the person in yrs. => "))
if age>=18:
      print("you are eligible to vote")

elif age<18:
      age=18-age
      print ("you are underage to vote")
      print("you have ",age, "to vote")
