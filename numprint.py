# program to print numbers from 1 to 100 and only those which are not
# divisible by 3 and 5
i=1
j=1
num=1
while (i<=10):
    while j<=10:
        if(num%3==0):
            print(end="  ")
        elif(num%5==0):
            print(end="  ")
        else:
            print(num,end=" ")
        num=num+1
        j=j+1
    print()
    i=i+1
    j=1