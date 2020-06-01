class Node:
    def __init__(self,data):
        self.data = data                      # Node Data
        self.next = None                      # Pointer to Next Node
        self.prev = None                      # Pointer to Previous Node

class doubleLinkedList():
    def __init__(self):
        self.head = None                      # First Node in Linked List


# ------------------ Inserting Node in Linked List -------------------
    def insertItem(self,data):
        newNode = Node(data)
        if self.head == None:
            self.head = newNode
        else:
            temp = self.head
            while temp.next != None:
                temp = temp.next
            temp.next = newNode
            newNode.prev = temp


# ------------------ Node Insertion at STARTING of Linked List -----------------
    def insertItemAtBegining(self,data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode


# ------------------ Node Insertion in BETWEEN two nodes of Linked List -----------------
    def insertBetweenTwoItems(self,middleData,data):
        newNode = Node(data)
        temp = self.head
        while temp.data != middleData:
            temp = temp.next
        last = temp.next
        newNode.prev = temp
        newNode.next = last
        temp.next = newNode


# ------------------ Node Removal from END of Linked List -----------------
    def removeFromEnd(self):
        if self.head == None:
            return
        else:
            temp = self.head
            while temp.next.next != None:
                temp = temp.next
            temp.next = None


# ------------------ Node Removal from an INDEX of Linked List -----------------
    def removeItemAtIndex(self,index):
        temp = self.head
        if index == 0:
            temp = self.head.next
            self.head = temp
            return
        else:
            i = 0
            while i != index:
                i += 1
                temp = temp.next
            last = temp.prev
            before = temp.next
            last.next = temp.next
            before.prev = last
            temp = None


# ------------------ Traversing a Linked List -----------------
    def traverseList(self):
        temp = self.head
        if self.head is None:
            print("List is Empty")
            return
        while temp:
            print("-> " + str(temp.data), end=" ")
            temp = temp.next
        print()


# ------------------ Testing the Linked List -----------------
lnkdList = doubleLinkedList()
lnkdList.insertItem(5)
lnkdList.insertItem(10)
lnkdList.insertItem(20)
lnkdList.insertItem(30)

print("Original Linked List : ",end="\t")
lnkdList.traverseList()

lnkdList.insertItemAtBegining(40)
print("Linked List after Insertion at the Begining : ",end=" ")
lnkdList.traverseList()

lnkdList.insertBetweenTwoItems(20,50)
print("Linked List after Insertion Between Two nodes : ",end=" ")
lnkdList.traverseList()

lnkdList.removeFromEnd()
print("Linked List after Removing item from the END : ",end=" ")
lnkdList.traverseList()

lnkdList.removeItemAtIndex(2)
print("Linked List after Removing item at an INDEX : ",end=" ")
lnkdList.traverseList()