class Node:
    def __init__(self,data):
        self.data = data                        # Node Data
        self.next = None                        # Pointer to Next Node

class doublyLinkedList:
    def __init__(self):
        self.head = None                        # First Node in Linked List


# ------------------ Inserting Node in Linked List -------------------
    def insertItem(self,item):
        newNode = Node(item)
        if self.head == None:
            self.head = newNode
            newNode.next = self.head
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = newNode
            newNode.next = self.head


# ------------------ Node Insertion at END of Linked List ----------------
    def insertAtEnd(self,item):
        newNode = Node(item)
        temp = self.head
        while temp.next != self.head:
            temp = temp.next
        temp.next = newNode
        newNode.next = self.head
        

# ------------------ Node Insertion at BEGINING of Linked List ----------------
    def insertAtBeginingOfList(self,item):
        newNode = Node(item)
        temp = self.head
        while temp.next != self.head:
            temp = temp.next
        temp.next = newNode
        newNode.next = self.head
        self.head = newNode


# ------------------ Node Removal from BEGINING of Linked List -----------------
    def removeItemAtBeginingOfList(self):
        if self.head == None:
            return
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = self.head.next
            self.head = temp.next


# ------------------ Node Removal from END of Linked List -----------------
    def removeItemFromEnd(self):
        if self.head == None:
            return
        else:
            temp = self.head
            while temp.next.next != self.head:
                temp = temp.next
            temp.next = self.head


# ------------------ Node Removal from an INDEX of Linked List -----------------
    def removeItemAtIndex(self,index):
        temp = self.head
        prev_node = self.head
        if index == 0:
            self.removeItemAtBeginingOfList
        else:
            i = 0
            while i != index:
                i += 1
                prev_node = temp
                temp = temp.next
            next_node = temp.next
            prev_node.next = next_node
            temp = None
            

# ------------------ Traversing the Linked List -----------------
    def traverseList(self):
        temp = self.head
        if self.head is None:
            print("List is Empty")
            return
        while temp:
            print("-> " + str(temp.data), end=" ")
            temp = temp.next
            if(temp == self.head):
                print()
                break


# ------------------ Testing the Linked List -----------------
lnkdList = doublyLinkedList()
lnkdList.insertItem(3)
lnkdList.insertItem(6)
lnkdList.insertItem(9)
lnkdList.insertItem(10)
lnkdList.insertItem(11)

print("Original Linked List : ",end="\t")
lnkdList.traverseList()

lnkdList.insertAtEnd(12)
print("Linked List after Insertion at the end : ",end=" ")
lnkdList.traverseList()

lnkdList.insertAtBeginingOfList(0)
print("Linked List after Insertion at the Begining : ",end=" ")
lnkdList.traverseList()

lnkdList.removeItemAtBeginingOfList()
print("Linked List after Removing item from the Begining : ",end=" ")
lnkdList.traverseList()

lnkdList.removeItemFromEnd()
print("Linked List after Removing item from the END : ",end=" ")
lnkdList.traverseList()

lnkdList.removeItemAtIndex(2)
print("Linked List after Removing item at an INDEX : ",end=" ")
lnkdList.traverseList()
            
