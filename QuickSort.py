#Partition et Quicksort
import time
import random

def Partition(A, p, r):
    alt = True
    x = A[r]
    i = p-1
    for j in range(p,r):
        if A[j] == x:
            alt = not alt
        if (A[j] == x and alt) or A[j] < x:
            i+= 1
            A[i], A[j] = A[j], A[i]
    A[r], A[i+1] = A[i+1], A[r]
    return i+1

def Quicksort(A, p, r):
    if p < r:
        q = Partition(A, p, r)
        Quicksort(A, p, q-1)
        Quicksort(A, q+1, r)

def RandomizedPartition(A, p, r):
    i = random.randint(p,r)#tirer aléatoirement un entier entre p et r
    A[r], A[i] = A[i], A[r]
    return Partition(A,p,r)

def RandomizedQuicksort(A, p, r):
    if p < r:
        q = RandomizedPartition(A, p, r)
        RandomizedQuicksort(A, p, q-1)
        RandomizedQuicksort(A, q+1, r)

def RandomizedQuicksort_iterative(A):
    S = [(0, len(A)-1)]#contiendra un couple
    while len(S) > 0:
        p, r = s.pop()
        if p < r:
            q = RandomizedPartition(A, p, r)
            S.append((p, q-1))
            S.append((q+1, r))

#A = [4,7,2,4,2,8,3,1,9,1]
n = int(1e6)
A = list(range(n))
#print(A)
p = 0
r = len(A)-1
t_0 = time.time() # début chrono
#Quicksort(A, p, r)
RandomizedQuicksort(A, p, r)
t_1 = time.time() # fin chrono
print("{} s".format(round(t_1-t_0, 2)))
#print(A)
