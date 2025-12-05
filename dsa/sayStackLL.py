class Saynode:
    def __init__(self,value):
        self.value = value
        self.next = None

class Saystack:
    def __init__(self):
        self.size = 0
        self.head = None

    def push(self,value):
        new_node = Saynode(value)
        if self.head == None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.size += 1
    
    def peek(self):
        return self.head.value
    
    def pop(self):
        popped_node = self.head
        self.head = self.head.next
        self.size -=1
        return popped_node.value
    

    
    def stacksize(self):
        return self.size

a = Saystack()
a.push(77)
a.push(78)
a.push(34)
a.push(71)
a.push(153)
print(a.peek())
print(a.stacksize())
print("Popped Element", a.pop())
print(a.peek())
print(a.stacksize())
