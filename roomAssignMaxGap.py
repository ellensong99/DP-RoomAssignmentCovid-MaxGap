import numpy as np
line1 = input().split()
line2 = input().split()
n = int(line1[0])
t = int(line1[1])
L = int(line1[2])
Q = [int(i) for i in line2]
Sum = [ [0]*(n+1) for i in range(n+1)]
G = [[0]*(n+1) for i in range(n+1)]
M = [[0]*(t+1) for i in range(n+2)]
Cut = [[0] * (t+1) for i in range(n+2)]
infty = L + 1

def PSum(i, j):
   if i == j:
       Sum[i][i] = Q[i-1]
   elif i > j:
       Sum[i][j] = -1
   else:
       Sum[i][j] = Q[i-1] + Sum[i+1][j]

def GetG(i, j):
   if i > j:
       G[i][j] = -1
   elif i == j:
       G[i][j] = L+1
   else:
       G[i][j] = (L-Sum[i][j])/float(j-i)

def DP():
    for i in range(n+1, 0, -1): ##start from M[n, t]=>M[n, t-1]
        for k in range(t, -1, -1):
            if n-i+1 <= k: # |i, ..., n| <= k
                M[i][k] = L+1
            elif k == 0:
                M[i][k] = -1
            else:
                maxi = M[i+1][k-1] # let i be alone, put i+1,...,n into k-1 rooms => kth room has 1 person
                mini = L+1
                idx = i
                #if k == 1: ## now we have M(i, k) k = 1 prob: when i + 1 = n means 1 ppl left, but 0 room left
                for j in range(i+1, n-k+2): #print(i, j, k, maxi)  put j+1, ...,n into k-1 rooms put i,..,j into the same room => kth room has j-i+1 ppl
                   if maxi < min(M[j+1][k-1], G[i][j]):
                       maxi = min(M[j+1][k-1], G[i][j])
                       idx = j
                M[i][k] = maxi
                Cut[i][k] = idx - i + 1
                                
def MinGap():
   for i in Q:
       if i > L:
           print("IMPOSSIBLE")
           return
   for i in range(n, 0, -1):
       for j in range(n, 0, -1):
           PSum(i,j)
           GetG(i,j)
   DP()
   ret = M[1][t] 
   if ret < 0:
       print("IMPOSSIBLE")
   else:
       print(ret)
       s = t
       pos = 1
       numList = []
       while s > 0:
           num = Cut[pos][s]
           numList.append(num)
           pos = pos + num
           s = s-1
       print(*numList, sep=" ")
           
MinGap()

