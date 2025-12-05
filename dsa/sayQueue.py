"""
Docstring for dsa.sayQueue

Enqueue
Dequeue
Peek
isEmpty
Size
"""


queue = []

# Enqueue

queue.append(10)
print("Top Element is:",queue[0])
if queue:
    print("Not empty")
else:
    print("Empty")

print("Length of the Queue is:",len(queue))
popped_element = queue.pop(0)
print("Popped Element:",popped_element)

if queue:
    print("Not empty")
else:
    print("Empty")


# CLASS Implementation

class Queueclass:
    def __init__(self):
        self.queue = []
        self.size = 0
    
    def enqueue(self,element):
        self.queue.append(element)
        self.size += 1
    
    def peek(self):
        if self.queue:
            return self.queue[0]
        else:
            return "Empty queue"
    
    def dequeue(self):
        if self.queue:
            self.queue.pop(0)
            self.size -= 1
        else:
            return "Empty Queue"
    
    def isEmpty(self):
        if self.queue:
            return "Not Empty queue"
        else:
            return "Empty queue"
    
    def whatSize(self):
        return len(self.queue)
    
obj1 = Queueclass()
obj1.enqueue(12)
obj1.enqueue(15)
obj1.enqueue(22)
print(obj1.peek())

print(obj1.queue)  

obj1.dequeue()

print(obj1.queue)

