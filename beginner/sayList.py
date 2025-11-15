print("Hello World");

#LISTS

"""

Consider you are writing the all the events your school students are going to participate in kalolsavam.
Same person can attend multiple events, you write their name twice, but that doesn't matter
since you are concerned about the number of events only. Based on the situation, person name can be changed.
Since the no of items counted, there is an order in the list

"""

x = ["apple","orange","banana"];
print(x)
x.append(5)
print(x)
print(len(x))
print(type(x))

#list() is a contstructor

fruits = list(("jackfruit","pomagranade"))
print(fruits)

# Membership testing => if x in set

print(fruits[0])
print(fruits[-1])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

f = ["apple","orange"]
print(f[1])
f[1] = "kiwi"
print(f)

g = ["A","B","C","D","E"]
h = ["F","G"]
g[2:4] = h
print(g)

thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon","Gattarmelon","Bootermelon","Shootermelon"]
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.insert(0,"Gatterlemnon")
print(thislist)
thislist.append("Shootermelon")
print(thislist)

thislist.extend(thislist)
print(thislist)

d = {"name" : "nolan","age" : 55}
thislist.extend(d)
print(thislist)

thislist.remove("Shootermelon");
print(thislist)

thislist.pop()
print(thislist)
thislist.pop(1)
print(thislist)

# Remove is a method while del is a keyword

thislist.clear()
print(thislist)

del thislist



# Range Funtion syntax = range(start, stop, step)
# Range funtion returns an iterable. 
# Iterable is an object with set of elements which can return them one by one which makes it iterable through a loop

x = range(3, 17, 2)
for i in x:
    print(i)

thislist = ["apple", "banana", "cherry","Torry","Curry"]

# Here the len funtion returns the length of the list
# Range funtion takes it and creates an iterable starting from zero, incrementing with one and end before the length
# this iterable is iterated in the print statement

for j in range(len(thislist)): 
    print(thislist[j])

print("WHILE LOOP")
print(len(thislist))
i = 0
while i < len(thislist):
    print(thislist[i])
    i += 1

#list with fruit name which as r in it

thislist = ["apple", "banana", "cherry","Torry","Curry"]
newlist = []

for i in thislist:
    if "r" in i:
        newlist.append(i)

print("printing new list")
print(newlist)


squarelist = []
for i in range(1,11):
    squarelist.append(i**2)

print(squarelist)


print("list comprehension with if condition")
squarelist = [i**2 for i in range(1,17) if i % 2 != 0]
print(squarelist)

# list comprehension creates a list in one line, the list elements to be listed is the first expression
# and this is followed by a for loop with iterable
# optionally, after the iterable, a conditional statement can also be provided.
# This will be for a range of iterable, perform the expression and add it in the list if the condition is satisfied



fruitlist = ["apple","orange","cherry","torry","curry","worry","sorry"]

newlist = [i.upper() for i in fruitlist if "r" in i ]
print(newlist)

newlist = ["Hello Dude" for i in fruitlist if "r" in i ]
print(newlist)


#Sorting

fruitlist = ["apple","orange","cherry","torry","curry","worry","sorry"]

fruitlist.sort()
print(fruitlist)

fruitlist.sort(reverse=True)
print(fruitlist)

fruitlist = ["apple","orange","cherry","torry","curry","worry","sorry",10,11,12]

fruitlist.sort(key=str)
print(fruitlist)

#here the key value will be used to sort

def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)

x = -10
print(abs(x))


global y
y = 10
def funcTest(n):
    return n

thislist = [3,56,78,4,7]
thislist.sort(key=funcTest)
print(thislist)

# Sort funtion is case sensitive. upper cases has more precedence.
# str.lower can be used as key to make the sort case insensitive

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)

# Both list and copy funtions performs the copy action but, copy is a list function meanwhile list is a built in function

a = [1,2,3]
b = a.copy()
c = list(a)

print("This is B :", b)
print("This is C :", c)

# Joining two methods

a = [1,2,3]
b = [4,5,6,7]

c = a + b
print(c)

for i in b:
    a.append(i)
print("Using append method, List A is now : ", a)

#LIST METHODS

a = [1,2,3,4,5,6,7]
b = [1,2,3,4]

b.append(5)
print(b)

a.extend(b)
print(a)

a.insert(2,4)
a.insert(2,4)
print(a)

print(a.index(7))

a.pop()
print(a)

a.pop()
print(a)

a.pop(1)
print(a)

a.remove(4)
print(a)

a = [x for x in a if x!=4]
print(a)

mylist = ['apple', 'banana', 'cherry']
mylist[0] = 'kiwi'
print(mylist[1])

list1 = [1,2]
list2 = [3,4]
list3 = [5,6,7]

list3 = list1 + list2
print(list3)