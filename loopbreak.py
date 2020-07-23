av=10
x=int(input("How many candies you want"))
i=1

while i<=x:
    if (i>av):
       print("We are out of stock")
       break # to jump out from the  loop
    print("candy")
    i+=1
print("bye")