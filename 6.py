import numpy as np
arr=np.array([[1,2,3],[1,2,3]])
print("sum of the array",arr.sum())
print("max of the array",arr.max())
print("min of the array",arr.min())
print("max of the array",arr.max(axis=1))
print("min of the array",arr.min(axis=1))
print("cumsum of the array",arr.cumsum(axis=1))
print("average of the array",np.average(arr))
