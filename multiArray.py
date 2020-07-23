#array using numpy
from numpy import *
arr=array([1,2,3,4,5.0])
print(arr.dtype)
arr1=linspace(0, 15,20) # Example of linspace to create array
print(arr1)
arr2=arange(1,15,2)# array using arange()
print(arr2)
arr3=logspace(1,40,5)# array using logspace() for logarathmi c array
print(arr3)
arr4=ones(5) # creating array using ones which have all one
print(arr4)
arr5=zeros(5) # creating array using zeros which have all zeros
print(arr5)