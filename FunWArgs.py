def person(name,age=20):# passing default value
    print(name)
    print(age)


person('safi',30) #Position arguments
person(age=32,name='saf') #keywords arguments
person('Faiek')# function call with default value

def sum(a,*b): # passing multiple arguments as tuple
    c=a
    for i in b:
        c=c+i

    print(c)
    print(a)
    print(b)
sum(5,9,87)

