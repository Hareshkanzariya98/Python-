import numpy as np
arr=np.array([[1,2,3,4],[5,6,7,8],[0,0,0,0]])
a=len(arr)
b=len(arr)+1
for i in range(a):
    for j in range(b):
        print(arr[i,j])