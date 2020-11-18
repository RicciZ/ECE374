def quadratic_probing_insert(T,k):
    i = 0
    while (i < 21):
        j = (k+i+3*i**2) % 21
        if T[j] == None:
            T[j] = k
            return j
        else:
            i = i + 1

def double_hashing_insert(T,k):
    i = 0
    while (i < 21):
        j = (k + i*(1 + (k % 20))) % 21
        if T[j] == None:
            T[j] = k
            return j
        else:
            i = i + 1

m = 21
quadratic = [None]*m
double = [None]*m
A = [7, 22, 44, 43, 27, 89, 30, 64, 85]
for i in A:
    quadratic_probing_insert(quadratic,i)
    double_hashing_insert(double,i)

print("hash insertion with quadratic probing")
print(quadratic)
print("hash insertion with double hashing")
print(double)