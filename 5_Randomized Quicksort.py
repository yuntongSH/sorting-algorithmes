"""
Randomized-Partition(A, p, r)
    i = Random(p, r)
    exchange A[r] with A[i]
    return Partition(A, p, r)

Partition(A, p, r)
    x = A[r]
    i = p - 1
    for j = p to r - 1
        if A[j] <= x
            i = i + 1
            exchange A[i] with A[j]
    exchange A[i + 1] with A[r]
    return i + 1

Randomized-Quicksort(A, p, r)
    if p < r
        q = Randomized-Partition(A, p, r)
        Randomized-Quicksort(A, p, q - 1)
        Randomized-Quicksort(A,p,r)

"""

import random

def RandomizedPartition(A, p, r):
    i = random.randint(p, r)
    A[r], A[i] = A[i], A[r]
    return Partition(A, p, r)

def Partition(A, p, r):
    alt = True
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] == x:
            alt = not alt
        if (A[j] == x and alt) or A[j] < x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[r], A[i + 1] = A[i + 1], A[r]
    return i + 1

def RandomizedQuicksort(A, p, r):
    if p < r:
        q = RandomizedPartition(A, p, r)
        RandomizedQuicksort(A, p, q-1)
        RandomizedQuicksort(A, q+1, r)

def RandomizedQuicksort_iterative(A):
    S = [(0, len(A)-1)] # Initialize a stack with a tuple containing the start and end indices of the array
    while len(S) > 0:
        p, r = S.pop() # Pop a pair (start index, end index) from the stack
        if p < r:
            q = RandomizedPartition(A, p, r)
            S.append((p, q-1)) # Push the indices of the left subarray onto the stack
            S.append((q+1, r)) # Push the indices of the right subarray onto the stack

n = int(1e2)
A = list(range(n))

RandomizedQuicksort(A, 0, len(A)-1)
RandomizedQuicksort_iterative(A)
print (A)



