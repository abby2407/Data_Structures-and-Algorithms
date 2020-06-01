class Node:
    def __init__(self,data):
        self.data = data                        # Node Data
        self.next = None                        # Pointer to Next Node
        self.prev = None                        # Pointer to Previous Node

class circularDoublyLinkedList:
    def __init__(self):
        self.head = None                        # First Node in Linked List


# ------------------ Inserting Node in Linked List -------------------
    def insertItem(self,item):
        newNode = Node(item)
        if self.head == None:
            self.head = newNode
            newNode.next = self.head
            newNode.prev = self.head
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            newNode.next = temp.next
            temp.next = newNode
            newNode.prev = temp


# ------------------ Traversing a Linked List -----------------     
    def traverseList(self):
        temp = self.head
        if self.head is None:
            print("List is Empty")
        while temp:
            print("-> "+ str(temp.data),end=" ")
            temp = temp.next
            if(temp == self.head):
                break

lnkdList = circularDoublyLinkedList()
lnkdList.insertItem(5)
lnkdList.insertItem(10)
lnkdList.insertItem(15)

print("Original Linked List : ",end="\t")
lnkdList.traverseList()
