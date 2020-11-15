import hashlib as hl

class Direct_Table:
    def __init__(self,K,m):
        self.T = [None]*m
        for i in K:
            self.T[i] = i

    def search(self,k):
        return self.T[k]

    def insert(self,x):
        self.T[x] = x

    def delete(self,x):
        self.T[x] = None

    def findmax(self):
        maxx = 0
        for i in self.T:
            if i != None:
                if i > maxx:
                    maxx = i
        return maxx

K = [2,3,5,8]
dt = Direct_Table(K,10)
print(dt.T)
print(dt.findmax())

class Direct_Table_bit_vector:
    def __init__(self,K,m):
        self.T = [0]*m
        for i in K:
            self.T[i] = 1

    def search(self,k):
        if self.T[k]:
            return k
        else:
            return None

    def insert(self,x):
        self.T[x] = 1

    def delete(self,x):
        self.T[x] = 0

def linear_probing_insert(T,k):
    i = 0
    while (i < 11):
        j = (k + i) % 11
        if T[j] == None:
            T[j] = k
            return j
        else:
            i = i + 1

def quadratic_probing_insert(T,k):
    i = 0
    while (i < 11):
        j = (k+i+3*i**2) % 11
        if T[j] == None:
            T[j] = k
            return j
        else:
            i = i + 1

def double_hashing_insert(T,k):
    i = 0
    while (i < 11):
        j = (k + i*(1 + (k % 10))) % 11
        if T[j] == None:
            T[j] = k
            return j
        else:
            i = i + 1

m = 11
linear = [None]*m
quadratic = [None]*m
double = [None]*m
A = [10, 22, 31, 4, 15, 28, 17, 88, 59]
for i in A:
    linear_probing_insert(linear,i)
    quadratic_probing_insert(quadratic,i)
    double_hashing_insert(double,i)

