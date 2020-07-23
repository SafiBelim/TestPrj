from numpy import *
m1 = matrix('1 2 3;6 4 5;7 8 9')
m2 = matrix('1 2 3;6 8 5;9 4 5')

print('Matrix 1:-\n', m1)
print('Matrix 2:\n', m2)
m3 = m1 + m2
print('Addition of matrix:-\n', m3)
m4 = m1 * m2
print('Multiplication of matrix:-\n', m4)
