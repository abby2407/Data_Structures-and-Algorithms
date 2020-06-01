class Queue:
    def __init__(self):
        self.queue = []
    
    def enqueue(self,item):
        return self.queue.append(item)

    def dequeue(self):
        if len(self.queue) < 1:
            return None
        else:
            return self.queue.pop()

    def size(self):
        return len(self.queue)

q = Queue()
q.enqueue(3)
q.enqueue(6)
q.enqueue(9)
print(q.size())
q.dequeue()
print(q.size())

#-----------------*--------------------*------------------*-----------

# Queue using Linked List
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedListQueue:
    def __init__(self):
        self.front = self.rear = None

    def isempty(self):
        return self.front == None

    def enqueueList(self,item):
        temp = Node(item)

        if self.rear == None:
            self.front = self.rear = temp
        else:
            self.rear.next = temp
            self.rear = temp

    def dequeueList(self):
        if self.isempty():
            return
        temp = self.front
        self.front = temp.next
        temp = None

        if self.front == None:
            self.rear = None

    def size(self):
        temp = self.front
        l = 0
        while temp != None:
            l += 1
            temp = temp.next

        return l


Myqueue = LinkedListQueue()
Myqueue.enqueueList(4)
Myqueue.enqueueList(8)
Myqueue.enqueueList(12)
print(Myqueue.size())
Myqueue.dequeueList()
print(Myqueue.size())

