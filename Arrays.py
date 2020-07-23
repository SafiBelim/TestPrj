from array import *
vals = array('i', [5, 9, -8, 4, 2])
newArr=array(vals.typecode,(a*a for a in vals)) # creating new array with old array values
#print(vals.buffer_info())
#print(vals.typecode)
#print(vals) normal print array
#vals.reverse()
for i in vals:
    print(i, end=" ")  # printing array with loop

print()
i = 0
while i < len(newArr):
    print(newArr[i], end=" ")
    i += 1
