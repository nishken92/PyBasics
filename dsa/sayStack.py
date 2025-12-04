# STACKS
# Last in First out (LIFO). A stack of pancakes.

stack = []

#PUSH
stack.append(10)
stack.append(20)
stack.append(30)
stack.append(40)
stack.append(50)

#PEEK
print(stack[-1])

#POP
poppedElement = stack.pop()
print(stack)
print(poppedElement)
removedElement = stack.remove(40)
print(stack)

# To check isEmpty
tack = []
boolValue = bool(tack)
print(boolValue)

# SIZE

print(len(stack))

# STACK IMPLEMENTATION AS CLASS

class Stack():
    def __init__(self):
        self.stack = []
    #stack = []
    def push(self, element):
        self.stack.append(element)

a = Stack()
a.push(10)
print(a.stack)

b = Stack()
b.push(25)
print(b.stack)

# dunder methods in python are class methods which get executed automatically once an object
# for the class is created. 


# Advantage of Linked List stack is it's of fixed size.


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

a = Node(12)
b = Node(4)
c = Node(7)
d = Node(10)
a.next = b
b.next = c
c.next = d

# Note, here a.next = b means the a.next attribute will contain the object reference of b

print(a.data,b.data,c.data,d.data)

