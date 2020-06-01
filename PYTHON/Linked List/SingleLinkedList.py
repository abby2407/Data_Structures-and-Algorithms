class Node:
    def __init__(self,data):
        self.data = data                                     # Node Data
        self.next = None                                     # Pointer to Next Node    

class singleLinkedList:
    def __init__(self):
        self.head = None                                     # First Node in Linked List


# ------------------ Inserting Node in Linked List -------------------
    def insertItem(self,item):
        newNode = Node(item)
        if self.head == None:
            self.head = newNode
        else:
            temp = self.head
            while temp.next != None:
                temp = temp.next
            temp.next = newNode


# ------------------ Node Insertion at END of Linked List ----------------
    def insertAtEndOfList(self,item):
        newNode = Node(item)
        temp = self.head
        while temp.next != None:
            temp = temp.next
        temp.next = newNode


# ------------------ Node Insertion at STARTING of Linked List -----------------
    def insertAtBeginingOfList(self,item):
        newNode = Node(item)
        newNode.next = self.head
        self.head = newNode


# ------------------ Node Insertion in BETWEEN two nodes of Linked List -----------------
    def insertBetweenTwoItems(self,middleItem,item):
        newNode = Node(item)
        temp = self.head
        while temp.data != middleItem:
            temp = temp.next
        nextNode = temp.next
        temp.next = newNode
        newNode.next = nextNode


# ------------------ Node Removal from END of Linked List -----------------
    def removeItemAtEndOfList(self):
        if self.head == None:
            return
        else:
            temp = self.head
            while temp.next.next != None:
                temp = temp.next
            temp.next = None


# ------------------ Node Removal from BEGINING of Linked List -----------------
    def removeItemAtBeginingOfList(self):
        if self.head == None:
            return
        else:
            self.head = self.head.next


# ------------------ Function to check if a Linked List is PALINDROME or not -----------------
    def isPalindrome(self):
        palin = True
        lst = []
        temp = self.head
        while temp != None:
            lst.append(temp.data)
            temp = temp.next

        tmp = self.head
        while tmp != None:
            i = lst.pop()
            if tmp.data == i:
                palin = True
            else:
                palin = False
                break
            tmp = tmp.next
        return palin


# ------------------ Merge a Linked List into another Linked List at alternate positions -----------------
    def mergingTwoLinkedList(self,lst):
        lst1 = self.head
        lst2 = lst.head

        while lst1 != None and lst2 != None:
            lst1Next = lst1.next
            lst2Next = lst2.next

            lst1.next = lst2
            lst2.next = lst1Next

            lst1 = lst1Next
            lst2 = lst2Next
        
        lst.head = lst2


# ------------------ An interesting method to print REVERSE of a Linked List -----------------
    def reverseList(self,n):
        i = 0
        temp = self.head
        print("Reverse of the Merged Linked List is: ", end="\n")
        while temp != None:
            j = 0
            while (j < 2 * (n - i)):
                print(end=" ")
                j = j + 1
            print(temp.data,end="\r")
            temp = temp.next
            i = i + 1


# ------------------ Traversing a Linked List -----------------
    def traverseList(self):
        temp = self.head
        while temp != None:
            print("-> " + str(temp.data), end=" ")
            temp = temp.next
        print()


# ------------------ SIZE a Linked List -----------------
    def sizeOfList(self):
        temp = self.head
        size = 0
        while temp != None:
            size += 1
            temp = temp.next
        return size


# ------------------ Testing the Linked List -----------------
lnkdList = singleLinkedList()

   # for Testing singly Linked List
lnkdList.insertItem(20)
lnkdList.insertItem(40)
lnkdList.insertItem(60)

print("Original Linked List : ",end="\t")
lnkdList.traverseList()

lnkdList.insertAtBeginingOfList(80)
print("Linked List after Insertion at the Begining : ",end=" ")
lnkdList.traverseList()

lnkdList.insertAtEndOfList(100)
print("Linked List after Insertion at the end : ",end=" ")
lnkdList.traverseList()

lnkdList.insertBetweenTwoItems(40,120)
print("Linked List after Insertion Between Two Nodes : ",end=" ")
lnkdList.traverseList()

lnkdList.removeItemAtEndOfList()
print("Linked List after Removing item from the END: ",end=" ")
lnkdList.traverseList()

lnkdList.removeItemAtBeginingOfList()
print("Linked List after Removing item from the Begining : ",end=" ")
lnkdList.traverseList()

print("Is this Linked List Palindrome : " + str(lnkdList.isPalindrome()))


    # Testing for merging Two Linked List
lnkdList2 = singleLinkedList()

lnkdList2.insertItem(3)
lnkdList2.insertItem(6)
lnkdList2.insertItem(9)
lnkdList2.insertItem(12)

lnkdList.mergingTwoLinkedList(lnkdList2)
print("First Linked List after Merging wiht second List : " ,end=" ")
lnkdList.traverseList()
print()

size = lnkdList.sizeOfList()
print("Size of the Merged Linked List is : ",size,end="\n")
print()
lnkdList.reverseList(size)