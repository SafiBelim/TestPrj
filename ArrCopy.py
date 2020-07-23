from numpy import *
arr1=array([1,2,3,4,5])
arr2=array([6,1,9,3,2])
arr3=arr1+arr2# addition of two arrays
print(arr3)
print(sin(arr1))# sin value of array
print(log(arr2))# log value of array
print(sum(arr2))# sum of array
print(min(arr1))# min value of array

print(concatenate([arr1, arr2])) # concatenate array

arr4=arr1 # copying array
print(arr4)
print(id(arr1))
print(id(arr4))
arr5=arr1.copy()# for deep copy when changing one array value it not change another