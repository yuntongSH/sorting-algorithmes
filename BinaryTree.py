"""
Binary Trees

def Explore_rec(x):
| print(x.key)
| if x.left != NIL: #cela veut dire que x a un enfant gauche
| | Explore(x.left)
| end-if
| if x.right != NIL: #cela veut dire que x a un enfant droit
| | Explore(x.right)
| end-if
end

def Explore_iter(x):
| S <- {x}
| while |S| > 0:
| | x <- S.pop()
| | print(x.key)
| | if x.left != NIL:
| | | S.push(x.left)
| | end-if
| | if x.right != NIL:
| | | S.push(x.right)
| | end-if
end
"""
class tree:
    def __init__(self):
        self.root = None

class node:
    def __init__(self, key):
        self.key = key
        self.p = None #parent du noeud
        self.left = None #enfant gauche
        self.right = None #enfant droit

    def show(self):
        print("key : {}".format(self.key), end= " ")
        if self.p is not None:
            print("key parent : {}".format(self.p.key), end=" ")
        if self.left is not None:
            print("key left : {}".format(self.left.key),end=" ")
        if self.right is not None:
            print("key right : {}".format(self.right.key),end=" ")
        print() #retour à la ligne

    def addchild(self, direction, key):
        x = node(key)
        x.p = self
        if direction == "left":
            if self.left is not None:
                print("Existing left child")
                return
            self.left = x
        if direction == "right":
            if self.right is not None:
                print("Existing right child")
                return
            self.right = x

    def explore_rec(self):
        self.show()
        if self.left is not None:
            self.left.explore_rec()
        if self.right is not None:
            self.right.explore_rec()

    def explore_iter(self):
        S = [self]
        while len(S) > 0:
            x = S.pop()
            x.show()
            if x.right is not None:
                S.append(x.right)
            if x.left is not None:
                S.append(x.left)

T = tree()
T.root = node(3)
T.root.addchild("left", 7)
T.root.addchild("right", 9)
T.root.right.addchild("left",2)
T.root.explore_rec()
print("---------------------------")
T.root.explore_iter()
