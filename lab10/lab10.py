# brute force
# to test if a is b's subsequence
def isSubsequence(a,b):
    i = j = 0
    while i < len(a) and j < len(b):
        if a[i] == b[j]:
            i += 1
        j += 1
    return i==len(a)

def LCS_bf(X,Y):
    subX = []
    m = len(X)
    n = len(Y)
    lcs = None
    maxlen = 0
    for i in range(2**m):
        temp = ""
        for j in range(m):
            if i & (1<<j):
                temp += X[j]
        subX.append(temp)
    for i in subX:
        if len(i) > maxlen and isSubsequence(i,Y):
            maxlen = len(i)
            lcs = i
    return lcs,maxlen

# dynamic programming
def LCS_dp(X,Y):
    m = len(X)
    n = len(Y)
    if m==0 or n==0:
        return None,0
    c = [[0]*(n+1) for i in range(m+1)]
    b = [[None]*(n+1) for i in range(m+1)]
    for i in range(1,m+1):
        for j in range(1,n+1):
            if X[i-1] == Y[j-1]:
                c[i][j] = 1 + c[i-1][j-1]
                b[i][j] = [i-1,j-1]
            elif c[i][j-1] <= c[i-1][j]:
                c[i][j] = c[i-1][j]
                b[i][j] = [i-1,j]
            else:
                c[i][j] = c[i][j-1]
                b[i][j] = [i,j-1]
    maxlen = c[m][n]
    lcs = ""
    while b[m][n] != None:
        if b[m][n] == [m-1,n-1]:
            lcs = X[m-1] + lcs
        m,n = b[m][n]
    return lcs,maxlen

X = "ABCBDAB"
Y = "BDCABA"
print(f"the result by brute force: {LCS_bf(X,Y)}")
print(f"the result by dynamic programming: {LCS_dp(X,Y)}")