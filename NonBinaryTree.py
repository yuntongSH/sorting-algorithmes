"""
left-child, right-sibling
lc: leftchild
rc: right sibling
"""

class tree:
    def __init__(self):
        self.root = None

    def count(self):
        if self.root == None:
            return 0
        else:
            return self.root.explore_iter()

    def countleaves(self):
        if self.root is None:
            return 0
        return self.root.countleaves()

class node:
    def __init__(self, key):
        self.key = key
        self.p = None # parent
        self.lc = None # left-child
        self.rs = None # right sibling

    def show(self):
        print("key : {}".format(self.key), end=" ")
        if self.p is not None:
            print("keyp : {}".format(self.p.key), end=" ")
        if self.lc is not None:
            print("keylc : {}".format(self.lc.key), end=" ")
        if self.rs is not None:
            print("keyrs : {}".format(self.rs.key), end=" ")
        print() #retour à la ligne

    def addleftmostchild(self, k):
        #créer un enfant pour le noeud courant, et le positionne ke plus à gauche, c'est-à-dire à gauche de l'enfant gauche s'il existe.
        #création de l'enfant x au noeud courant
        x = node(k)
        x.p = self
        x.rs = self.lc
        self.lc = x

    def explore_rec(self):
        self.show()
        x = self.lc
        while x is not None:
            x.explore_rec()
            x = x.rs

    def explore_iter(self):
        visited = 0
        S = [self]
        while S:
            visited += 1
            x = S.pop()
            x.show()
            x = x.lc
            while x is not None:
                S=[x]+S
                x = x.rs
        return visited

    def countleaves(self):
        leaves = 0
        S = [self]
        while S:
            x = S.pop()
            if x.lc == None:
                leaves += 1
            x.show()
            x = x.lc
            while x is not None:
                S=[x]+S
                x = x.rs
        return leaves

#Programme principal
T = tree()
T.root = node(2)
T.root.addleftmostchild(11)
T.root.addleftmostchild(8)
T.root.addleftmostchild(6)
T.root.lc.rs.addleftmostchild(4)
T.root.lc.rs.rs.addleftmostchild(9)
T.root.explore_rec()
print("-----------------------------")
T.root.explore_iter()

print("nb elt : {}".format(T.count()))
print("nb leaves : {}".format(T.root.countleaves()))


U = tree()

print("nb elt empty tree : {}".format(U.count()))
print("nb leaves empty tree : {}".format(U.countleaves()))
