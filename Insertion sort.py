"""
Insertion sort

INSERTION-SORT(A)

for j = 2 to A.length
	  key = A[j]
      i = j - 1
	  while i > 0 and A[i] > key
		  A[i + 1] = A[i]
		  i = i - 1
	  A[i + 1] = key
      
"""

def InsertionSort(A):
    for j in range(1, len(A)):
        key = A[j]
        i = j -1
        while i > -1 and  A[i] > key:
            A[i + 1] = A[i]
            i -= 1 
        A[i + 1] = key
        
# Example usage
A = [5, 2, 9, 1, 5, 6]
InsertionSort(A)
print(A)  # Output will be the sorted list


"""
Rewrite the INSERTION-SORT procedure to sort into nonincreasing instead of nondecreasing order.

 for j = 2 to A.length
    key = A[j]
    i = j − 1
    while i > 0 and A[i] < key
        A[i + 1] = A[i]
        i = i − 1
    A[i + 1] = key

"""
def insertion_sort_descending(A):
    # Loop through each element in the array starting from the second element
    for j in range(1, len(A)):  # Adjusted index to start from 1 (second element in Python)
        key = A[j]
        i = j - 1
        while i > -1 and A[i] < key:
            A[i + 1] = A[i]
            i -= 1
        A[i + 1] = key

# Example usage
A = [12, 11, 13, 5, 6]
insertion_sort_descending(A)
print(A)
