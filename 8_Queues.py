"""
Enqueue(Q, x)
    Q[Q.tail] = x
    if Q.tail == Q.length
        Q.tail = 1
    else Q.tail = Q.tail + 1
    
Dequeue(Q)
    x = Q[Q.head]
    if Q.head == Q.length
        Q.head = 1
    else Q.head = Q.head + 1
    return x

"""
class CircularQueue:
    def __init__(self, size):
        self.Q = [None] * size
        self.head = 0
        self.tail = 0
        self.size = size
        self.count = 0  # To keep track of the number of elements in the queue

    def enqueue(self, x):
        if self.count == self.size:
            raise Exception("Queue is full")
        self.Q[self.tail] = x
        self.tail = (self.tail + 1) % self.size
        self.count += 1

    def dequeue(self):
        if self.count == 0:
            raise Exception("Queue is empty")
        x = self.Q[self.head]
        self.head = (self.head + 1) % self.size
        self.count -= 1
        return x

# Example usage
if __name__ == "__main__":
    # Create a CircularQueue with capacity for 3 elements
    queue = CircularQueue(3)
    
    # Enqueue elements
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    
    # Trying to add another element will raise an exception
    try:
        queue.enqueue(40)
    except Exception as e:
        print(e)  # Output: Queue is full

    # Dequeue elements
    print(queue.dequeue())  # Output: 10
    print(queue.dequeue())  # Output: 20

    # Enqueue more elements
    queue.enqueue(40)
    queue.enqueue(50)

    # Dequeue the rest of the elements
    print(queue.dequeue())  # Output: 30
    print(queue.dequeue())  # Output: 40
    print(queue.dequeue())  # Output: 50

    # Trying to dequeue from empty queue
    try:
        print(queue.dequeue())
    except Exception as e:
        print(e)  # Output: Queue is empty