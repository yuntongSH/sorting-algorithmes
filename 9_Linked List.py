"""
List-Search(L, k)
    x = L.head
    while x <> NIL and x.key <> k
        x = x.next
    return x

List-Insert(L, x)
    x.next = L.head
    if L.head <> NIL
        L.head.prev = x
    L.head = x
    x.prev = NIL
    
List-Delete(L, x)
    if x.prev <> NIL
        x.prev.next = x.next
    else L.head = x.next
    if x.next <> NIL
        x.next.prev = x.prev
        
"""
class LIST:
    def __init__(self):
        self.head = None
        
    def show(self):
        x = self.head
        while x != None:
            if x.prev == None:
                keyprev = "aucun"
            else:
                keyprev = x.prev.key
            if x.next == None:
                keynext = "aucun"
            else:
                keynext = x.next.key
            print(keyprev,x.key,keynext)
            x = x.next
            
    def insert(self,x):
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
        while x != None and x.key != k:
            x = x.next
        return x
        
    def delete(self, x):
        if isinstance(x, element) == False:
            print("Erreur de type sur x dans insert")
            return
        if self.head == None:
            print("Erreur, liste vide")
            return
        if x.prev != None:
            x.prev.next = x.next
        else:
            self.head = x.next
        if x.next != None:
            x.next.prev = x.prev
            
    
class element:
    def __init__(self,key):
        self.key = key
        self.prev = None
        self.next = None
        
    def show(self):
        if self.prev == None:
            keyprev = "aucun"
        else:
            keyprev = self.prev.key
        if self.next == None:
            keynext = "aucun"
        else:
            keynext = self.next.key
        print(keyprev, self.key, keynext)
        

L = LIST()

L.insert(element(3))
L.insert(element(2))        
L.insert(element(1))
L.show()

#suppression de l'élément de clé 2
L.delete(L.search(2))
L.show