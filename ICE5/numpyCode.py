import numpy as np


a=np.array([1,2,3,4,5,6,7,8,9])
b=np.array([9,8,7,6,5,4,3,2,1])
c = a+b
print(c)

z = np.random.random((10,10))
print(z)
print("Min value:",z.min())
print("Max value:",z.max())
print("-------------------")
s = np.random.randint((10,10))
print(s)
print("-------------------")

rows  = 10
cols = 10
low = 22
high = 37
step = 2

matrix = np.random.choice([x for x in range(low,high,step)],rows*cols)
matrix.resize(rows,cols)

print(matrix)
print("Min value:",matrix.min())
print("Max value:",matrix.max())