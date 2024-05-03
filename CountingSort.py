def CountingSort(A, k):
    B = list(A)
    C = []
    for i in range(0, k+1):
        C.append(0)
    for j in range(0, len(A)):
        C[A[j]] += 1
    for i in range(1, k+1):
        C[i] += C[i-1]
    for j in range(len(A) - 1, -1, -1):
        B[C[A[j]] - 1] = A[j]
        C[A[j]] -= 1
    return B

#A = [2,3,4,0,2,3,3,0,3]
#k = 5 #valeur max de A
#best case
n = int(1e5)
A = []
for i in range(n):
    A.append(random.randint(0,n//10))
    if k < A[i]:
        k = A[i]
#worst cas
A = [0, int(1e5), 1]
k = max(A)
B = CountingSort(A,k)
print("ok")
#print(B)
