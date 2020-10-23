mxavg=0
mxiiavg=0
mgavg=mt=0

n=0
mx1=mxt=mx2=mx3=mx4=mx5=0
mxii1=mxiit=mxii2=mxii3=mxii4=mxii5=0
mg1=mg2=mg3=mg4=0
while (n!=-1):
    n=int(input("enter the student no (-1 to exit) => "))
    print("CODES FOR STREAMS :-  \n c -> Commerce \n n-> Non medical \n m -> medical \n a-> Arts")
    print(format('*','*<15'), "ENTRIES SECTION",format('*','*<15'))

    print(format('*','*<15'), "Class X Details",format('*','*<15'))
    mx1=int (input("Enter marks 1 "))
    mx2=int (input("Enter marks 2 "))
    mx3=int (input("Enter marks 3 "))
    mx4=int (input("Enter marks 4 "))
    mx5=int (input("Enter marks 5 "))
    mxt=mx1+mx2+mx3+mx4+mx5
    mxavg=mxt/5

    print(format('*','*<15'), "Class XII Details",format('*','*<15'))
    mxii1=int (input("Enter marks 1 "))
    mxii2=int (input("Enter marks 2 "))
    mxii3=int (input("Enter marks 3 "))
    mxii4=int (input("Enter marks 4 "))
    mxii5=int (input("Enter marks 5 "))
    ch=input("enter code for stream")
    mxiit=mxii1+mxii2+mxii3+mxii4+mxii5
    mxiiavg=mxiit/5

    print(format('*','*<15'), "GRADUATION Details",format('*','*<15'))
    mg1=int (input("Enter marks 1 "))
    mg2=int (input("Enter marks 2 "))
    mg3=int (input("Enter marks 3 "))
    mg4=int (input("Enter marks 4 "))
    mgt=mg1+mg2+mg3+mx4
    mgavg=mgt/4

    print(format('*','*<15'), "POST GRADUATION Details",format('*','*<15'))
    ch1=input("Enter the code for stream opted")
    if (mxavg>=80):
        if (mxiiavg>=80):
            if (ch1==ch):
                if (mgavg>=70):
                    print("you are eligible for admission")
            elif (ch1!=ch):
                mgt=mgt-0.05*mgt

                elif (mgavg>=70):
                    print("you are eligible for admission")

                else :
                    print("NOT ELIGIBLE")
                    break

            else :
                print("NOT ELIGIBLE")
                break

        else :
            print("NOT ELIGIBLE")
            break
            
        
    

    
    
    
