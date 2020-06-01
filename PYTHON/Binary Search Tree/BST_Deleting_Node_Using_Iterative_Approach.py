class Node:
    def __init__(self,data):
        self.data = data                            # Node Data
        self.left = None                            # Pointer to LEFT Node
        self.right = None                           # Pointer to RIGHT Node
        self.parent = None                          # Pointer to PARENT Node

class binaryTree1:
    def __init__(self):
        self.root = None                            # Pointer to ROOT Node


# ------------------ Inserting Node in a Tree -------------------
    def insertNode(self,data):
        if self.root == None:
            self.root = Node(data)
        else:
            self._insert(self.root,data)

    def _insert(self,temp,data):
        if data < temp.data:
            if temp.left == None:
                temp.left = Node(data)
                temp.left.parent = temp
            else:
                self._insert(temp.left,data)
        elif data > temp.data:
            if temp.right == None:
                temp.right = Node(data)
                temp.right.parent = temp
            else:
                self._insert(temp.right,data)
        else:
            print("data already in tree")


# ------------------ Function to Check whether the specified data is available in the tree or not!! -------------------
    def findValue(self,data):
        if self.root == None:
            return None
        else:
            return self._findValue(self.root,data)

    def _findValue(self,temp,data):
        if data == temp.data:
            return temp
        elif data < temp.data and temp.left != None:
            return self._findValue(temp.left,data)
        elif data > temp.data and temp.right != None:
            return self._findValue(temp.right,data)


# ------------------ Deleting a Node from Tree using Iterative Approach -------------------
    def deleteNode(self,data):
        if self.findValue(data) == None:
            return print("data not present in tree")
        else:
            return self._delete(self.findValue(data))

    def _delete(self,node):

        def num_of_children(node):
            num_children = 0
            if node.left != None: num_children += 1
            if node.right != None: num_children += 1

            return num_children

        def min_value_node(node):
            temp = node
            while temp.left != None:
                temp = temp.left
            return temp

        node_parent = node.parent
        node_children = num_of_children(node)

        if node_children == 0:
            if node_parent != None:
                if node_parent.left == node:
                    node_parent.left = None
                else:
                    node_parent.right = None
            else:
                self.root = None

        if node_children == 1:
            if node.left != None:
                child = node.left
            else:
                child = node.right

            if node_parent != None:
                if node_parent.left == node:
                    node_parent.left = child
                else:
                    node_parent.right = child
            else:
                self.root = None

            child.parent = node_parent

        if node_children == 2:
            last_node = min_value_node(node)
            node.data = last_node.data
            self._delete(last_node)


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
tree = binaryTree1()
tree.insertNode(10)
tree.insertNode(6)
tree.insertNode(16)
tree.insertNode(4)
tree.insertNode(7)
tree.insertNode(3)
tree.insertNode(5)
tree.insertNode(8)
tree.insertNode(14)
tree.insertNode(17)
tree.insertNode(13)
tree.insertNode(15)
tree.insertNode(18)

print("Original BST Tree : ",end="\t")
tree.preOrderTraversal()

tree.deleteNode(14)
print("Tree Structure After Deleting a Node : ",end=" ")
tree.preOrderTraversal()

        
 