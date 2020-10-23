i=0;
c = input("c for car \n t fro truck or bus \n s for scooter \nPlease Enter the code for the vehicle : ");

tot=0
if (c=='c'):
    print("YOU HAVE PARKED A CAR")
    tot = 10*t
    print("The total amt is : ", tot)
    
if (c=='t'):
    print("you have parked a bus / a truck")
    tot=20*t
    print("The total amt is : ", tot)
if (c=='s'):
    print("you have parked a scooter")
    tot=5*t
    print("The total amt is : ", tot)



t=int (input("Enter the no of hours"))    
    
