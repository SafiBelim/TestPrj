n1=int(input("Enter 1st no."))
n2=int(input("Enter 2nd no."))
print("Provide your mathematical operation from the given lists \n 1.Addition \n 2. Subtraction \n 3.Multiplication \n 4.Division")
ch=int(input("Enter your choice from above menu"))
if(ch==1):
      print("Addition is ",n1+n2)
elif(ch==2):
      print("Subtraction is ", n1-n2)
elif(ch==3):
      print("Multiplication is",n1*n2)
elif(ch==4):
      print("Devision is ",n1/n2)
else:
      print("Undefined choice")