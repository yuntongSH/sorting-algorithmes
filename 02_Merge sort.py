"""
Merge sort
p: the starting index of the subarray
r: the ending index of the subarray

MergeSort(A,p,r)
    if p < r 
        q = [(p + r)/2]
        MergeSort(A,p,q)
        MergeSort(A, q + 1, r)
        Merge(A, p, q, r)
        
Merge(A,p,q,r)
    n1 = q - p +1
    n2 = r - q
    let L[1..n1+1] and R[1..n2+1] be new arrays
    for i = 1 to n1
        L[i] = A[ p + i - 1]
    for j = 1 to n2
        R[j] = A[q + j]
    L[n1 + 1] = ∞
    R[n2 + 1] = ∞
    i = 1
    j = 1
    for k = p to r
        if L[i] <= R[j]
            A[k] = L[i]
            i = i + 1
        else A[k] = R[j]
            j = j + 1
"""

import math

def MergeSort(A, p, r):
    if p < r:
        q = (p + r) // 2
        MergeSort(A, p, q)
        MergeSort(A, q + 1, r)
        Merge(A, p, q, r)

def Merge(A, p, q, r):
    L = A[p : q + 1]
    L.append(math.inf)  # Use infinity as a sentinel value
    i = 0
    R = A[q + 1 : r + 1]
    R.append(math.inf)  # Use infinity as a sentinel value
    j = 0
    for k in range(p, r + 1):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1

# Example usage:
A = [3, 5, 2, 9, 10, 1, 6]
MergeSort(A, 0, len(A) - 1)
print(A)
