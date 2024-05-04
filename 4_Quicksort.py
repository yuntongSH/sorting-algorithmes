# -*- coding: utf-8 -*-
"""
partition(A, p, r)
    x = A[r]
    i = p - 1
    for j = p to r - 1
        if A[j] <= x
            i = i + 1
            exchange A[i] with A[j]
    exchange A[i + 1] with A[r]
    return i + 1

QuickSort(A,p,r)
    if p < r
        q = partition(A, p, r)
        QuickSort(A, p, q - 1)
        QuickSort(A, q+1, r)
"""

def partition(A, p, r):
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

def quicksort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quicksort(A, p, q - 1)
        quicksort(A, q + 1, r)

A=[3,7,5,4,2,8,5,1,9,5]
quicksort(A,0,len(A)-1)

print (A)

