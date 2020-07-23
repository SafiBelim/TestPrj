from functools import reduce # for reduce
def is_even(n):
    return n%2==0
nums=[3,2,6,8,4,6,2,9,7]
even = list (filter(lambda n:n%2==0,nums)) # anonymous function
doubles=list(map(lambda n:n*2,even)) # map function
sum=reduce(lambda a,b:a+b , doubles) # reduce function

print(even)
print(doubles)
print(sum)