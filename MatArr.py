from numpy import *

arr1 = array([
    [1, 2, 3, 4, 5, 7],
    [4, 5, 6, 3, 2, 8]
])
print(arr1.ndim)  # to check array dimension
print(arr1.shape)  # to know how many rows and columns
arr2 = arr1.flatten()  # Convert 2 dimension into 1 dimesion
print(arr2)
arr3 = arr2.reshape(3, 4)  # convert 1d array to 2d array
# passing no. of rows and columns
print(arr3)
arr4 = arr2.reshape(2, 2, 3)  # convert 1d array to 3d array
print('3d array')
print(arr4)
