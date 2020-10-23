import random
n=20
to_be_guessed = int (n*random.random())+1
guess=0
while guess != to_be_guessed :
    guess=int (input ("number is : "))
    if guess >0:
        if guess > to_be_guessed:
            print("guess to large")
        elif guess <to_be_guessed:
              print("guess too small")

    else:
        print ("sorry you are giving up it was ",  to_be_guessed)
        break
else :
    print ("congoyou have made it ",)
                
