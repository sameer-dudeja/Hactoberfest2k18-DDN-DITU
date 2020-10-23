def display(name,*favsubject):
    print("'\n'")
    print(name,"likes to read => ")
    for sub in favsubject:
        print(sub,end="")



display("Gornash", "cse", "btech", "ece", "mechanical")
display("Gorna", "cse", "btech", "ece", "mechanical", "everything else")
