from numpy import *
arr1 = array([
    [1,2,3,4],
    [4,5,6,7]
])
#m=matrix(arr1)
m = matrix('1 2 3;4 5 6;7 8 9')# creating matrix without array
print(m.min()) # minimum value
print(m.max())# max value of matrix
m1=matrix('1 2 3;6 4 5; 1 6 7')
m2=matrix('1 2 3;6 8 5;2 6 7')
m3=m1*m2 # multiply matrices
print(m3)