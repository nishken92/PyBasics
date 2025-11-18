# Class object

class Person:
    def __init__(self,i,j,k):
        self.i = i
        self.j = j
        self.k = k
        

d = Person(25,35,45)
print(d.i,d.j,d.k)



# Instance object

class Numbers:
    pass

Numbers.counter = 10
print(type(Numbers.counter))