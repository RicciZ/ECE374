import numpy as np

def partition(A,p,r):
    x = A[r]
    i = p-1
    for j in range(p,r):
        if A[j] >= x:
            i += 1
            A[i],A[j] = A[j],A[i]
    A[i+1],A[r] = A[r],A[i+1]
    return i+1

def Hoar_partition(A,p,r):
    x = A[p]
    i = p-1
    j = r+1
    while True:
        while True:
            j -= 1
            if A[j] <= x:
                break
        while True:
            i += 1
            if A[i] >= x:
                break
        if i < j:
            A[i],A[j] = A[j],A[i]
        else:
            return j

def quicksort(A,p,r):
    if p < r:
        q = Hoar_partition(A,p,r)
        quicksort(A,p,q)
        quicksort(A,q+1,r)

A = np.random.randint(0,100,25)
print(A)
quicksort(A,0,len(A)-1)
print(A)

