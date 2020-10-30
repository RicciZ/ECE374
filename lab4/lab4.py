import numpy as np

def binary_search(vec,i,j,v):
    if i>j:
        return -1
    mid = (j-i)//2+i
    if vec[mid] == v:
        return mid
    elif vec[mid] > v:
        return binary_search(vec,i,mid,v)
    else:
        return binary_search(vec,mid+1,j,v)

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


vec = np.random.randn(25)
mergesort(vec,5)
print(vec)
for i in vec:
    print(binary_search(vec,0,len(vec)-1,i))
print(binary_search(vec,0,len(vec)-1,99))



def matrix_divide(A):
    midr = len(A) // 2
    midc = len(A[0]) // 2
    a = A[:midr,:midc]
    b = A[:midr,midc:]
    c = A[midr:,:midc]
    d = A[midr:,midc:]
    return a,b,c,d

def matrix_merge(a,b,c,d):
    r1 = len(a)
    r2 = len(c)
    c1 = len(a[0])
    c2 = len(b[0])
    A = np.zeros((r1+r2,c1+c2))
    A[:r1,:c1] = a
    A[:r1,c1:] = b
    A[r1:,:c1] = c
    A[r1:,c1:] = d
    return A

def Strassen(A,B):
    if len(A) == 1:
        return np.array([A*B])
    else:
        a,b,c,d = matrix_divide(A)
        e,f,g,h = matrix_divide(B)

        P11 = f-h
        P21 = a+b
        P31 = c+d
        P41 = g-e
        P51 = a+d
        P52 = e+h
        P61 = b-d
        P62 = g+h
        P71 = a-c
        P72 = e+f

        P1 = Strassen(a,P11)
        P2 = Strassen(P21,h)
        P3 = Strassen(P31,e)
        P4 = Strassen(d,P41)
        P5 = Strassen(P51,P52)
        P6 = Strassen(P61,P62)
        P7 = Strassen(P71,P72)

        r = P5+P4-P2+P6
        s = P1+P2
        t = P3+P4
        u = P5+P1-P3-P7

        return matrix_merge(r,s,t,u)


A = np.random.rand(8,8)
B = np.random.rand(8,8)
res_np = np.matmul(A,B)
res_Strassen = Strassen(A,B)
print(res_np)
print(res_Strassen)
print(abs(res_np-res_Strassen)<0.0000001)