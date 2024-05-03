class LISTS:
    def __init__(self):
        self.nil = elements("sentinelle")
        self.nil.next = self.nil
        self.nil.prev = self.nil

    def show(self):
        x = self.nil.next
        while x != self.nil: # self.nil désigne la sentinelle
            x.show()
            x = x.next

    def insert(self, x):
        #vérification du typage de x
        if isinstance(x, elements) == False:
            print("Erreur de type sur x dans insert")
            return
        self.nil.next.prev = x
        x.prev = self.nil
        x.next = self.nil.next
        self.nil.next = x

    def search(self, k):
        x = self.nil.next
        while x != self.nil and x.key != k:
            x = x.next
        return x

    def delete(self, x):
        #vérification du typage de x
        if isinstance(x, elements) == False:
            print("Erreur de type sur x dans delete")
            return
        if self.nil.next != self.nil:
            print("Erreur, liste vide")
            return
        if x == self.nil: #cette condition est requise pour éviter de supprimer la sentinelle et ainsi corrompre la liste
            print("Tentative de la suppression de la sentinelle")
            return
        x.prev.next = x.next
        x.next.prev = x.prev


class elements: #pour LISTS avec sentinelle
    def __init__(self, key=None):
        self.key = key
        self.prev = self
        self.next = self

    def show(self):
        print(self.prev.key, self.key, self.next.key) #il y a toujours un prev : la sentinelle


L = LISTS()

L.insert(elements(3))
L.insert(elements(2))
L.insert(elements(1))
L.delete(L.search(3))
L.show()
print("la clef du dernier élément est : {}".format(L.nil.prev.key))
