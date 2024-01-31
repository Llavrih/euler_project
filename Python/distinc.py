import numpy as np

arr = []
for a in range(2, 101):
    for b in range(2, 101):
        arr.append(a**b)
print(len(arr))
print(len(np.unique(arr)))
