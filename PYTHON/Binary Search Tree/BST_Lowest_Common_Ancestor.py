
'''For two nodes, a and b, the lowest common ancestor c is the lowest node in the
                binary tree that has a and b as its descendants.'''
'''Two nodes may have more than one common ancestor, however, they can have only
                        one lowest common ancestor'''
'''
                                20
                               /  \
                              8     22
                            /  \   
                           4   12
                              /  \
                             10   14


        Input: LCA of 10 and 14
        Output:  12
        Explanation: 12 is the closest node to both 10 and 14 
        which is a ancestor of both the nodes.

        Input: LCA of 8 and 14
        Output:  8
        Explanation: 8 is the closest node to both 8 and 14 
        which is a ancestor of both the nodes.

        Input: LCA of 10 and 22
        Output:  20
        Explanation: 20 is the closest node to both 10 and 22 
        which is a ancestor of both the nodes.'''


class Node:
    def __init__(self,data):
        self.data = data                        # Node Data
        self.left = None                        # Pointer to LEFT Node
        self.right = None                       # Pointer to RIGHT Node

class lcaBST:
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


# ------------------ Recursive Approach -----------------
    def lCA_Recursive_Approach(self, n1, n2):
        temp = self.root
        if temp == None:
            return
        else:
            return self._lca_Recursive(temp, n1, n2)

    def _lca_Recursive(self,temp,n1,n2):
        if temp is None:
            return None
        if temp.data > n1 and temp.data > n2:
            return self._lca_Recursive(temp.left,n1,n2)
        if temp.data < n1 and temp.data < n2:
            return self._lca_Recursive(temp.right,n1,n2)
        
        return temp


# ------------------ Iterative Approach -----------------
    def lCA_Iterative_Approach(self, n1, n2):
        temp = self.root
        if temp == None:
            return
        else:
            return self._lca_Iterative(temp, n1, n2)
    
    def _lca_Iterative(self,temp, n1, n2):
        while temp != None:
            if temp.data > n1 and temp.data > n2:
                temp = temp.left
            elif temp.data < n1 and temp.data < n2:
                temp = temp.right
            else:
                break
        return temp


# ------------------ Testing the Binary search Tree Structure -----------------
tree = lcaBST()
tree.insertNode(6)
tree.insertNode(11)
tree.insertNode(4)
tree.insertNode(5)
tree.insertNode(10)
tree.insertNode(2)
tree.insertNode(12)

node = tree.lCA_Iterative_Approach(5,8)
print("The Lowest Common Ancestor of Given BST is : ",node.data)