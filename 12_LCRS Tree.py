"""
LCRS Tree
left child, right sibiling
occupation de mémore, excessive(feuille)

"""
class LCRSTree:
    def __init__(self):
        self.root = None
        
    def Count(self):
        if self.root is None:
            return 0
        else:
            return self.root.ExploreIterative()
    
    def CountLeaves(self):
        if self.root is None:
            return 0
        return self.root.CountLeaves()
        
class Node:
    def __init__(self, key):
        self.key = key
        self.p   = None #parent
        self.lc  = None #left-child
        self.rs  = None #right-sibiling
        
    def Show(self):
        print("key=", self.key, end= " ")
        if self.p != None:
            print("keyp=", self.p.key, end=" ")
        if self.lc != None:
            print("keylc=", self.lc.key, end=" ")
        if self.rs != None:
            print("keyrs=", self.rs.key, end=" ")
        print() #retoour à la ligne
        
    def Addleftmostchild(self,k): 
        #créer un enfant pour le noeud courant, et le positionne le plus à gauche, c'est-à-dire à gauche de l'enfant gauche s'il existe.
        x = Node(k)
        x.p = self
        x.rs = self.lc
        self.lc = x
        
    def ExploreRecursive(self):
        self.Show()
        x = self.lc
        while x != None:
            x.ExploreRecursive()
            x = x.rs
            
    def ExploreIterative(self):
        visited  = 0
        S = [self]
        while len(S) > 0:
            x = S.pop()
            visited += 1
            x.Show()
            x = x.lc
            while x != None:
                S.append(x)
                x = x.rs
        return visited
            
    def CountLeaves(self):
        leaves  = 0
        S = [self]
        while S:
            x = S.pop()
            if x.lc == None:
               leaves += 1
            x = x.lc
            while x != None:
               S.append(x)
               x = x.rs
        return leaves
               
#Programme principal
T = LCRSTree()
T.root = Node(2)
T.root.Addleftmostchild(11)
T.root.Addleftmostchild(8)
T.root.Addleftmostchild(6)
T.root.lc.rs.Addleftmostchild(4)
T.root.lc.rs.rs.Addleftmostchild(9)

print("Recursive Exploration of the Tree:")
T.root.ExploreRecursive()
print("-------------")

print("Iterative Exploration of the Tree:")
T.root.ExploreIterative()
print("-------------")

#print("Nb de noeuds dans T : ", T.root.ExploreIterative())
#print("Nb dr feuilles dans T : ", T.CountLeaves())

print("nb elt : {}".format(T.Count()))
print("nb leaves : {}".format(T.root.CountLeaves()))


U = LCRSTree()

print("nb elt empty tree : {}".format(U.Count()))
print("nb leaves empty tree : {}".format(U.CountLeaves()))