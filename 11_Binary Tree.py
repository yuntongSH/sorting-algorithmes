# -*- coding: utf-8 -*-
"""
Binary tree: Nodes and references

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

class BinaryTree:
    def __init__(self):
        self.root = None


class Node:
    def __init__(self, key):
        self.key = key
        self.p = None
        self.left = None
        self.right = None

    def Show(self):
        print("key=", self.key)
        if self.p is not None:
            print("key parent=", self.p.key, end=" ")
        if self.left is not None:
            print("key left=", self.left.key, end=" ")
        if self.right is not None:
            print("key right=", self.right.key, end=" ")
        print()  # New line for clarity

    def AddChild(self, direction, key):
        x = Node(key)
        x.p = self
        if direction == "left":
            if self.left is not None:
                print("Existing left child")
                return
            self.left = x
        elif direction == "right":
            if self.right is not None:
                print("Existing right child")
                return
            self.right = x

    def ExploreRecursive(self):
        self.Show()
        if self.left is not None:
            self.left.ExploreRecursive()
        if self.right is not None:
            self.right.ExploreRecursive()

    def ExploreIterative(self):
        S = [self]
        while len(S) > 0:
            x = S.pop()
            x.Show()
            if x.right is not None:
                S.append(x.right)
            if x.left is not None:
                S.append(x.left)


# Main execution starts here
T = BinaryTree()
T.root = Node(3)
T.root.AddChild("left", 7)
T.root.AddChild("right", 9)
T.root.right.AddChild("left", 2)
T.root.ExploreRecursive()
print("--------------------")
T.root.ExploreIterative()
print("--------------------")
T.root.Show()