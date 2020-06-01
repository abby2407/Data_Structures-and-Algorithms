
# ------------------ How to Handle Duplicates in a BST -------------------


'''In a Binary Search Tree (BST), all keys in left subtree of a key must be smaller and all keys
   in right subtree must be greater. So a Binary Search Tree by definition has distinct keys.'''


class Node:
    def __init__(self,data):
        self.data = data                            # Node Data
        self.count = 1                              # Data Count
        self.left = None                            # Pointer to LEFT Node
        self.right = None                           # Pointer to RIGHT Node

class DuplicatesInBST:
    def __init__(self):
        self.root = None                            # Pointer to ROOT Node


# ------------------ Inserting Node in a Tree -------------------
    def insertNode(self,data):
        if self.root == None:
            self.root = Node(data)
        else:
            self._insertNode(self.root,data)

    def _insertNode(self,temp,data):
        if temp.data == data:
            temp.count += 1
            return
        if data < temp.data:
            if temp.left is None:
                temp.left = Node(data)
            else:
                self._insertNode(temp.left,data)
        if data > temp.data:
            if temp.right is None:
                temp.right = Node(data)
            else:
                self._insertNode(temp.right,data)


# ------------------ Deleting a Node from Tree -------------------
    def deleteNode(self,data):
        if self.root == None:
            return
        else:
            self._deleteNode(self.root,data)

    def _deleteNode(self,temp,data):
        if temp == None:
            return temp
        if data < temp.data:
            temp.left = self._deleteNode(temp.left,data)
        elif data > temp.data:
            temp.right = self._deleteNode(temp.right,data)
        else:
            if temp.count > 1:
                temp.count -= 1
                return temp
            
            if temp.left == None:
                node = temp.right
                return node
            if temp.right == None:
                node = temp.left
                return node

            last_node = self.minValueNode(temp.right)
            temp.data = last_node.data
            temp.right = self._deleteNode(temp.right,last_node.data)

        return temp

    def minValueNode(self,temp):
        while temp.right != None:
            temp = temp.left
        return temp


# ------------------ PRE-ORDER Traversal of Tree -------------------
    def preOrderTraversal(self):
        if self.root == None:
            return 
        else:
            self._preOrderTraversal(self.root)
            print()

    def _preOrderTraversal(self,temp):
        print("-> " + str(temp.data), end=" ")
        if temp.left:
            self._preOrderTraversal(temp.left)
            if temp.right:
                self._preOrderTraversal(temp.right)
        elif temp.right:
            self._preOrderTraversal(temp.right)
            if temp.left:
                self._preOrderTraversal(temp.right)


# ------------------ Testing the Binary search Tree Structure -----------------
tree = DuplicatesInBST()
tree.insertNode(12)
tree.insertNode(10)
tree.insertNode(20)
tree.insertNode(9)
tree.insertNode(11)
tree.insertNode(10)
tree.insertNode(12)
tree.insertNode(12)

print("Pre-Order Traversal of Tree : ",end="\t")
tree.preOrderTraversal()

tree.deleteNode(12)
print("Tree Structure After Deleting a Node : ",end=" ")
tree.preOrderTraversal()

