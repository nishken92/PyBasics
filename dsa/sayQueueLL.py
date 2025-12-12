# QUEUE IMPLEMENTATION USING LINKED LIST

class Node:
    def __init__(self,value):
        self.value = value 
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0

    def enqueue(self,value):
        new_node = Node(value)
        if self.front == None:
            self.front = new_node
        if self.rear == None:
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        self.size += 1
    
    def peek(self):
        if self.size == 0:
            return "Empty Queue"
        else:
            return self.front.value
    
    def whatSize(self):
        return self.size
    
    def dequeue(self):
        if self.size == 0:
            return "Queue is empty"
        else:
            temp = self.front
            self.front = temp.next
            self.size -= 1
            if self.size == 0:
                self.rear = self.front = None
            return temp.value
            




a = Queue()

a.enqueue(10)
print("Size of the Queue is: ",a.whatSize())
print("Peek of the Queue is: ",a.peek())

a.enqueue(20)
print("Size of the Queue is: ",a.whatSize())
print("Peek of the Queue is: ",a.peek())

a.enqueue(50)
print("Size of the Queue is: ",a.whatSize())
print("Peek of the Queue is: ",a.peek())

a.enqueue(55)
print("Size of the Queue is: ",a.whatSize())
print("Peek of the Queue is: ",a.peek())

print(a.dequeue())
print("Size of the Queue is: ",a.whatSize())
print("Peek of the Queue is: ",a.peek())

print(a.dequeue())
print("Size of the Queue is: ",a.whatSize())
print("Peek of the Queue is: ",a.peek())

print(a.dequeue())
print("Size of the Queue is: ",a.whatSize())
print("Peek of the Queue is: ",a.peek())

print(a.dequeue())
print("Size of the Queue is: ",a.whatSize())
print("Peek of the Queue is: ",a.peek())

print(a.dequeue())
print("Size of the Queue is: ",a.whatSize())
print("Peek of the Queue is: ",a.peek())

a.enqueue(20)
print("Size of the Queue is: ",a.whatSize())
print("Peek of the Queue is: ",a.peek())

