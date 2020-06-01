  
  
'''A perfect binary tree is a type of binary tree in which every internal node
    has exactly two child nodes and all the leaf nodes are at the same level.'''


class Node:
    def __init__(self,data):
        self.data = data                        # Node Data
        self.left = None                        # Pointer to LEFT Node
        self.right = None                       # Pointer to RIGHT Node

class perfectBST:
    def __init__(self):
        self.root = None                        # Pointer to Root Node


# ------------------ Inserting Node in a Tree -------------------
    def insertNode(self,item):
        if self.root == None:
            self.root = Node(item)
        else:
            self._insert(item,self.root)

    def _insert(self,item,cur_node):
        if item < cur_node.data:
            if cur_node.left is None:
                cur_node.left = Node(item)
            else:
                self._insert(item,cur_node.left)
        elif item > cur_node.data:
            if cur_node.right is None:
                cur_node.right = Node(item)
            else:
                self._insert(item,cur_node.right)
        else:
            print("item already present in the tree")


# ------------------ Check whether a given binary tree is perfect or not -----------------
    def isPerfect(self):
        temp = self.root
        n = 0
        while temp != None:
            n += 1
            temp = temp.left
        return self.isPerfectTree(self.root,n)
    
    def isPerfectTree(self,temp,n,level = 0):
        if temp == None:
            return None
        if temp.left == None and temp.right == None:
            return (n == level + 1)
        if temp.left == None or temp.right == None:
            return False
        return self.isPerfectTree(temp.left,n,level + 1) and self.isPerfectTree(temp.right,n,level + 1)


# ------------------ Testing the Binary search Tree Structure -----------------
tree = perfectBST()
tree.insertNode(6)
tree.insertNode(11)
tree.insertNode(4)
tree.insertNode(5)
tree.insertNode(10)
tree.insertNode(2)
tree.insertNode(12)

print("is this BST Perfect: ",tree.isPerfect())