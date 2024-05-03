class LIST:
    def __init__(self):
        self.head = None

    def show(self):
        x = self.head
        while x is not None: # s'il est différent de None x existe donc la liste existe
            x.show()
            x = x.next

    def insert(self, x):
        #vérification du typage de x
        if isinstance(x, element) == False:
            print("Erreur de type sur x dans insert")
            return
        x.prev = None
        x.next = self.head
        if self.head != None:
            self.head.prev = x
        self.head = x

    def search(self, k):
        x = self.head
        while x is not None and x.key != k:
            x = x.next
        return x

    def delete(self, x):
        #vérification du typage de x
        if isinstance(x, element) == False:
            print("Erreur de type sur x dans delete")
            return
        if self.head is None:
            print("Erreur, liste vide")
            return
        if x.prev != None:
            x.prev.next = x.next
        else:
            self.head = x.next
        if x.next != None:
            x.next.prev = x.prev

class element:
    def __init__(self, key=None):
        self.key = key
        self.prev = None
        self.next = None

    def show(self):
        if self.prev == None:
            keyprev = "aucun" # clef du sprédecesseur s'il existe
        else:
            keyprev = self.prev.key
        if self.next == None:
            keynext = "aucun" # clef du successeur s'il existe
        else:
            keynext = self.next.key
        print(keyprev, self.key, keynext)        
        
                
L = LIST()

L.insert(element(3))
L.insert(element(2))
L.insert(element(1))
L.delete(L.search(3))
L.show()
L.insert(0) #erreur de typage
print(L.search(2))
print(L.search(5))
print(L.search(2).key)
print(L.search(3).key)
