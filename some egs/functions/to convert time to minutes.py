def convert (hr,mini):
    tot=(60*hr )+mini
    return tot




c=int (input("ENTER the format to be entered \n 1. for 24 hrs \n 2. 12 hrs =>"))


if (c==1):
    hr=int (input("ENTER hrs section =>"))
    if (hr<0 or hr >23):
        print("INVALID FORMAT")
        exit(0)
    mini =int (input("ENTER mins section =>"))
    if (mini >60 or mini<0):
        print("INVALID FORMAT")
        exit (0)
    else :
        print("time entered is "+str(hr)+":"+str(mini))
    print(convert (hr,mini))




if (c==2):
    hr=int (input("ENTER hrs section =>"))
    if (hr<1 or hr >12):
        print("INVALID FORMAT")
        exit(0)
    mini =int (input("ENTER mins section =>"))
    if (mini >60 or mini<0):
        print("INVALID FORMAT")
        exit (0)
    else :
        print("time entered is "+str(hr)+":"+str(mini))
    print(convert (hr,mini))    
