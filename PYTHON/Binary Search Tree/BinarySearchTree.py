class Node:
    def __init__(self,data):
        self.data = data                            # Node Data
        self.left = None                            # Pointer to LEFT Node
        self.right = None                           # Pointer to RIGHT Node

class binaryTree:
    def __init__(self):
        self.root = None                            # Pointer to ROOT Node


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


# ------------------ Deleting a Node from Tree using Recursive Approach -------------------
    def deleteNodeOfTree(self,item):
        temp = self.root
        if temp == None:
            return
        else:
            self._deleteNode(temp,item)

    def _deleteNode(self,temp,data):
        if data < temp.data:
            temp.left = self._deleteNode(temp.left,data)
        elif data > temp.data:
            temp.right = self._deleteNode(temp.right,data)
        else:
            if temp.left is None:
                val = temp.right
                temp = None
                return val
            elif temp.right is None:
                val = temp.right
                temp = None
                return val
            
            val = self.minValueNode(temp.right)

            temp.data = val.data
            temp.right = self._deleteNode(temp.right,temp.data)
        return temp

    def minValueNode(self,temp):
        cur_node = temp
        while cur_node.left is not None:
            cur_node = cur_node.left
        return cur_node


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


# ------------------ IN-ORDER Traversal of Tree -------------------
    def inOrderTraversal(self):
        if self.root == None:
            return 
        else:
            self._inOrderTraversal(self.root)
            print()
    
    def _inOrderTraversal(self,temp):
        if temp == None:
           return
        else:
            self._inOrderTraversal(temp.left)
            print("-> " + str(temp.data), end=" ")
            self._inOrderTraversal(temp.right)


# ------------------ POST-ORDER Traversal of Tree -------------------
    def postOrderTraversal(self):
        if self.root == None:
            return 
        else:
            self._postOrderTraversal(self.root)
            print()

    def _postOrderTraversal(self,temp):
        if temp == None:
            return
        else:
            self._postOrderTraversal(temp.left)
            self._postOrderTraversal(temp.right)
            print("-> " + str(temp.data), end=" ")


# ------------------ LEVEL-ORDER Traversal of Tree -------------------
    def levelOrderTraversal(self):
        if self.root == None:
            return 
        else:
            self._levelOrderTraversal(self.root)
            print()
    
    def _levelOrderTraversal(self,temp):
         queue = []

         queue.append(temp)
         while len(queue) > 0:
             print("-> " + str(queue[0].data), end=" ")
             node = queue.pop(0)
             if node.left != None:
                 queue.append(node.left)
             if node.right != None:
                queue.append(node.right)


# ------------------ fucntion to find HEIGHT of Tree -------------------
    def heightOfTree(self):
        if self.root == None:
            return 
        else:
            print("Height of tree: ",self._heightOfTree(self.root))
    
    def _heightOfTree(self,temp):
        if temp == None:
            return -1
        left_height = self._heightOfTree(temp.left)
        right_height = self._heightOfTree(temp.right)

        return 1 + max(left_height, right_height)


# ------------------ fucntion to find SIZE of Tree -------------------
    def sizeOfTree(self):
        if self.root == None:
            return 
        else:
            print("Size of Tree: ", self._sizeOfTree(self.root))
    
    def _sizeOfTree(self,temp):
        if temp == None:
            return 0
        else:
            return (self._sizeOfTree(temp.left) + 1 + self._sizeOfTree(temp.right))


# ------------------ Testing the Binary search Tree Structure -----------------
tree = binaryTree()
tree.insertNode(6)
tree.insertNode(11)
tree.insertNode(4)
tree.insertNode(5)
tree.insertNode(10)
tree.insertNode(2)
tree.insertNode(7)
tree.insertNode(8)

print("Pre-Order Traversal of Tree : ",end="\t")
tree.preOrderTraversal()

print("In-Order Traversal of Tree : ",end="\t")
tree.inOrderTraversal()

print("Post-Order Traversal of Tree : ",end="\t")
tree.postOrderTraversal()

print("Level-Order Traversal of Tree : ",end=" ")
tree.levelOrderTraversal()

tree.heightOfTree()
tree.sizeOfTree()

tree.deleteNodeOfTree(6)
print("Tree Structure After Deleting a Node : ",end=" ")
tree.preOrderTraversal()




