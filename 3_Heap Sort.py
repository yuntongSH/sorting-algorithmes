"""
#Top-down approach
Max-Heapify(A,i)
    l = Left(i)
    r = Right(i)
    if l <= A.heap-size and A[l] > A[i]
        largest = l
    else largest = i
    if r <= A.heap-size and A[r] > A[largest]
        largest = r
    if largest <> i
        exchange A[i] with A[largest]
        Max-Heapify(A.largest)

#Bottom-up approach
Build-Max-Heap(A)
    A.heap-size = A.length
    for i = ⌊A.length/2⌋ down to 1
        Max-Heapify(A,i)

HeapSort(A)
    Build-max-heap(A)
    for i = A.length downto 2
        exchange A[1] with A[i]
        A.heapsize = A.heapsize - 1
        Max-Heapify(A,1)
      
"""
def parent(i):
    if i <= 0:
        print("Erreur pas de parent")
        return
    return (i-1)//2

def left(i):
    return 2*i+1

def right(i):
    return 2*i+2

class heap:
    #a chaque création d'un objet de type heap il faut fournir un tableau
    def __init__(self, tab):
        self.length = len(tab)
        self.v = tab
        self.heapsize = 0

    def __str__(self):
        return "length : {}, v : {}, heapsize : {}".format(self.length, self.v, self.heapsize)

    def show(self):
        print(self)

    def MaxHeapify(self, i):
        l = left(i)
        r = right(i)
        if l < self.heapsize and self.v[l] > self.v[i]:
            largest = l
        else:
            largest = i
        if r < self.heapsize and self.v[r] > self.v[largest]:
            largest = r
        if largest != i:
            #utilisation d'un tuple
            self.v[i], self.v[largest] = self.v[largest], self.v[i]
            self.MaxHeapify(largest)

    def BuildMaxHeap(self):
        self.heapsize = self.length
        for i in range((self.length - 1)//2, -1, -1):
            self.MaxHeapify(i)
            
    def Heapsort(self):
        self.BuildMaxHeap()
        for i in range(self.length-1, 0, -1):
            self.v[i], self.v[0] = self.v[0], self.v[i]
            self.heapsize -= 1
            self.MaxHeapify(0)
            
