def greet(): # define a function
    print("Hello")

greet() # calling a function

def add_sub(x,y): # function with arguments
    c=x+y
    d=x-y
    return c,d # returning single value

result1,result2 = add_sub(5,4)
print("addition is", result1)
print("subtraction is", result2)