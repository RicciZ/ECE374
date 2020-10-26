def insertion_sort(vec):
    for i in range(1,len(vec)):
        num = vec[i]
        j = i - 1
        while j >= 0 and vec[j] < num:
            vec[j+1] = vec[j]
            j -= 1
        vec[j+1] = num

def linear_search(vec,v):
    for i in range(len(vec)):
        if vec[i] == v:
            return i
    return -1

def selection_sort(vec):
    for i in range(len(vec)-1):
        minn = i
        for j in range(i+1,len(vec)):
            if vec[j] < vec[minn]:
                minn = j
        vec[i],vec[minn] = vec[minn],vec[i]

def merge(vec,mid):
    i = 0
    j = mid + 1
    n = len(vec)
    new_vec = []
    while (i <= mid and j < n):
        if vec[i] > vec[j]:
            new_vec.append(vec[j])
            j += 1
        else:
            new_vec.append(vec[i])
            i += 1
    if (i > mid):
        new_vec.extend(vec[j:])
    else:
        new_vec.extend(vec[i:mid+1])
    vec = new_vec

def mergesort(vec,k):
    if len(vec) > k:
        insertion_sort(vec)
        return
    mid = len(vec) // 2
    mergesort(vec[0:mid],k)
    mergesort(vec[mid:],k)
    merge(vec,mid)

import numpy as np
vec = np.random.randn(20)
print(f"Before sorting {vec}")
print()
mergesort(vec,3)
print(f"After sorting {vec}")
