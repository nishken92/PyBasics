# TREES are hierarchical structures

# Binary tree are the tree structure where each node can have a maximum of two child nodes

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

a = TreeNode("A")
b = TreeNode("B")
c = TreeNode("C")
d = TreeNode("D")
e = TreeNode("E")
f = TreeNode("F")
g = TreeNode("G")

a.left = b
a.right = c
b.left = d
b.right = e
c.left = f
c.right = g

print(c.right.data)