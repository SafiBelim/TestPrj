def fact(x):
    f=1

    while x>=1:
        f=f*x
        x=x-1

    return(f)






n=int(input("Enter number"))
res=fact(n)
print("Factorial of given number is",res)