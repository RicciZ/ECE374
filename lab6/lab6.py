import numpy as np

def randomized_partition(A,p,r):
    rand = np.random.randint(p,r)
    A[r],A[rand] = A[rand],A[r]
    x = A[r]
    i = p-1
    for j in range(p,r):
        if A[j] <= x:
            i += 1
            A[i],A[j] = A[j],A[i]
    A[i+1],A[r] = A[r],A[i+1]
    return i+1

def randomized_select(A,p,r,i):
    if p == r:
        return A[p]
    q = randomized_partition(A,p,r)
    k = q - p + 1
    if i == k:
        return A[q]
    elif i < k:
        return randomized_select(A,p,q-1,i)
    else:
        return randomized_select(A,q+1,r,i-k)

A = np.random.randint(0,100,37)
print(A)
min = randomized_select(A,0,len(A)-1,1)
max = randomized_select(A,0,len(A)-1,len(A))
median = randomized_select(A,0,len(A)-1,(len(A)+1)//2)
print(f"min is {min}, max is {max}, median is {median}")
print(sorted(A))

