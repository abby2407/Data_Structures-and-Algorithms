
# ---------------stack using simple list ----------------------

class Stack():
    def __init__(self):
        self.stack = list()
    
    def push(self,item):
        self.stack.append(item)

    def pop(self):
        if len(self.stack) > 0:
            return self.stack.pop()
        else:
            return None
    
    def peek(self):
        if len(self.stack) > 0:
            return self.stack[len(self.stack) - 1]
        else:
            return None

    def __str__(self):
        return str(self.stack)

my_stack = Stack()
my_stack.push(5)
my_stack.push(10)
my_stack.push(15)
print(my_stack)
print(my_stack.pop())
print(my_stack.peek())
print(my_stack)

#-----------------*--------------------*------------------*-----------

# stack using Singly Linked List

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Stack1:
    def __init__(self):
        self.head = None

    def isempty(self):
        if self.head == None:
            return True
        else:
            return False

    def push(self,data):
        if self.head == None:
            self.head = Node(data)
        else:
            newnode = Node(data)
            newnode.next = self.head
            self.head = newnode

    def pop(self):
        if self.isempty():
            return None
        else:
            poppedNode = self.head
            self.head = self.head.next
            poppedNode.next = None
            return poppedNode.data

    def peek(self):
        if self.isempty():
            return None
        else:
            return self.head.data

    


MyStack = Stack1()
MyStack.push(2)
MyStack.push(4)
MyStack.push(6)
MyStack.pop()
print(MyStack)
