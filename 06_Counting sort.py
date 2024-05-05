"""
Counting-Sort(A, B, k)
    let C[0..k] be a new array
    for i = 0 to k
        C[i] = 0
    for j = 1 to A.length
        C[A[j]] = C[A[j]] + 1
    for i = 1 to k
        C[i] = C[i] + C[i - 1]
    for j = A.length downto 1
        B[C[A[j]]] = A[j]
        C[A[j]] = C[A[j]] - 1
        
"""

def CountingSort(A, k):
    B = list(A)
    C = [0] * (k + 1)
    for j in range(0, len(A)):
        C[A[j]] += 1
    for i in range(1, k + 1):
        C[i] += C[i - 1]
    for j in range(len(A) - 1, -1, -1):
        B[C[A[j]] - 1] = A[j]
        C[A[j]] -= 1
    return B

A = [2,3,4,0,2,3,3,0,3]
k = max(A)
B = CountingSort(A,k)
print(B)
