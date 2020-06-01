

class Node:
    def __init__(self,data):
        self.data = data                                # Node Data
        self.left = None                                # Pointer to LEFT Node
        self.right = None                               # Pointer to RIGHT Node

class QuesOnBST:
    def __init__(self):
        self.root = None                                # Pointer to ROOT Node


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


# ------------------ Fucntion to count leaf nodes in a binary tree -------------------
    def countOFLeafNodes(self):
        return self._countOfLeaf(self.root)

    def _countOfLeaf(self,temp):
        if temp == None:
            return 0
        if (temp.left is None) and (temp.right is None):
            return 1
        else:
            return self._countOfLeaf(temp.left) + self._countOfLeaf(temp.right)

# ------------------ Replace each node in binary tree with the sum of its inorder predecessor and successor -------------------
                                         
                                         # Solution Not Complete
        
    def findPredAndSucc(self):
        temp = self.root
        while temp != None:
            node = self._findPredAndSucc(temp)
            temp.data = node
            temp = temp.left

    def _findPredAndSucc(self,temp):
        pred = 0
        succ = 0
        if temp.left != None:
            last_node = temp.left
            while last_node.right != None:
                last_node = last_node.right
            
            pred = last_node.data

        if temp.right != None:
            last_node = temp.right
            while last_node.left != None:
                last_node = last_node.left
            
            succ = last_node.data

        return pred + succ



tree = QuesOnBST()
tree.insertNode(6)
tree.insertNode(11)
tree.insertNode(4)
tree.insertNode(5)
tree.insertNode(10)
tree.insertNode(2)
tree.insertNode(12)
print(tree.countOFLeafNodes())
tree.findPredAndSucc()



                


