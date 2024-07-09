import numpy as np

def find_common_values(arr1, arr2):
    common_values = np.intersect1d(arr1, arr2)
    return common_values

arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([4, 5, 6, 7, 8])

common_values = find_common_values(arr1, arr2)
print("Common values:", common_values)
