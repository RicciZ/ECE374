import numpy as np

def counting_sort(A):
    minx = min(A)
    maxx = max(A)
    k = maxx-minx+1
    C = []
    B = []
    for i in range(k):
        C.append(0)
    for i in A:
        C[i-minx] += 1
    for i in range(k):
        while C[i] > 0:
            B.append(i+minx)
            C[i] -= 1
    return B

A = np.random.randint(-10,10,20)
print(A)
A = counting_sort(A)
print(A)
