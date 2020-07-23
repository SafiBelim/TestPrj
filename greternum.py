a=int(input("Enter 1st number"))
b=int(input("Enter 2nd number"))
c=int(input("Enter 3rd number"))
if a>b:# simple if statement
    if a>c: # simple if multiple condition statement
        print("a is greater")
    else:
        print("c is greater")
elif b>c: # nested if statement
    print("b is greater")
else:
    print("c is greater")
