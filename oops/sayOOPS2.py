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


class Flower:
    pass

def smell(self):
    print("Smells good")

Flower.smell = smell

f = Flower()

f.smell()

# Method object.

"""
In the below example, function mouth is bounded to the class Human.
Argument self is given as method takes the calling object itself as an input first
Once the instance object x is created, it can call the mount function without any argument.
This is because any method will automatically pass the calling object as first argument.
In other words, if a function is called with N arguments by an object of P data attributes,
The function is actually called with N + P arguments. 
"""
class Human:
    def mount(self):
        print("Humans use mouth to speak")

x = Human()

x.mount()

# Class and Instance Variable


class Director:
    Language = "Tamil"
    name = "Mari Selvaraj"
    movie = "Bison"
    def __init__(self,name,movie):
        self.name = name
        self.movie = movie

Ranjith = Director("Pa.Ranjith","Madras")
Vetrimaran = Director("Vetrimaran","Vadachennai")

print(Ranjith.Language, Ranjith.name, Ranjith.movie)
print(Vetrimaran.Language, Vetrimaran.name, Vetrimaran.movie)
print(Director.name)

# Additional Topics

"""
Cinematographers is a class. useCamera is a function. A class variable is created
outside the class body and bound with the class. this variable is assined with the function calling.
Now the function can be called by refering the data attribute of the class. Instances of the 
class can also call the function by referencing the instance and class attribute.
"""

class Cinematographers:
    pass

def useCamera():
    return "Uses a Sony camera"

Cinematographers.x = useCamera()

print(Cinematographers.x)

a = Cinematographers()
b = Cinematographers()

print("PC Sreeram", a.x)
print("Balumahendra", b.x)


# Method calling Method with self

class Films:
    def filmName(self,name):
        name = name
        return name
    def dirName(self):
        print(self.filmName("Madras"))
    

a = Films()

a.dirName()
    

