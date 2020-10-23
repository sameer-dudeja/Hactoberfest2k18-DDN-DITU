def max(numbers):
    print("USER DEFINED FUNCTION MAX.....")
    large= -1
    for i in numbers:
        if (i>large):
            large=i
    return large

numbers=[9,-1,4,2,7]
print(max(numbers))
print("the sum of the nos = ",sum(numbers))
    
