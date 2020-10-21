import numpy as np

def insertionsort(vec):
    for i in range(1,len(vec)):
        num = vec[i]
        j = i - 1
        while j >= 0 and vec[j] > num:
            vec[j+1] = vec[j]
            j -= 1
        vec[j+1] = num

def merge(vec,mid):
    i = 0
    j = mid + 1
    n = len(vec)
    new_vec = []
    for _ in range(n):
        if j > n:
            new_vec.append(vec[i])
            i += 1
        elif i > mid:
            new_vec.append(vec[j])
            j += 1
        elif vec[i] > vec[j]:
            new_vec.append(vec[j])
            j += 1
        else:
            new_vec.append(vec[i])
            i += 1
    vec = new_vec

def mergesort(vec,k):
    if len(vec) > k:
        insertionsort(vec)
        return
    mid = len(vec) // 2
    mergesort(vec[0:mid],k)
    mergesort(vec[mid:],k)
    merge(vec,mid)


vec = np.random.randn(20)
print(f"Before sorting {vec}")
print()
mergesort(vec,3)
print(f"After sorting {vec}")