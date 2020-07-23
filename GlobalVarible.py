a=10
print(id(a))
def something():
    # global a to access a out of function
    a=9
    x=globals()['a']# accessing a from outside of function
    print(id(x))
    print("in fun ",a)
    globals()['a']=15


something()
print("outside fun",a)