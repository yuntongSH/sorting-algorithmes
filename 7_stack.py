"""
Stack-Empty(S)
    if S.top == 0
        return TRUE
    else return FALSE
    
Push(S, x)
    S.top = S.top + 1
    S[S.top] = x
    
Pop(S)
    if Stack-Empty(S)
        error "underflow"
    else S.top = S.top - 1
        return S[S.top + 1]
"""

class Stack:
    def __init__(self,n):
        self.length = n
        self.S = list(range(n))
        self.top = -1 #at creation, empty stack, pile vide
    
    def Show(self):
        for i in range(self.top + 1):
            print(self.S[i])
            
    def Push(self, x):
        if self.top == self.length - 1:
            print("Overflow error")
            return
        self.top += 1
        self.S[self.top] = x
        
    def StackEmpty(self):
        return self.top == -1

    def Pop(self):
        if self.StackEmpty():
            print("Underflow error")
            return
        self.top -= 1
        return self.S[self.top + 1]
    
S = Stack(7)

S.Push(15)
S.Push(6)
S.Push(2)
S.Push(9)
S.Show()

popped_item = S.Pop()
print(f"Popped item: {popped_item}")
S.Show()