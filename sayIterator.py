#Iterator is a list of countable number of elements which can be iterated

a = {1,2}
print(type(a))

# iter() and next() are inbuild methods of all the data type objects in python.
# Any data type can be turned into an iterable using iter() method
# next() method helps to access the set element.

myset = {"apple","banana","fig"}
myit = iter(myset)
print(next(myit))

# Result of the below will not be appearing as in the order of set, because set is unordered data structure

for i in myit:
    print(i)

# Result for the below will appear in order because list is an ordered data structure
mylist = ["Jaguar", "Audi", "Benz", "BMW", "Aston Martin"]
for i in mylist:
    print(i)

# Characters in a string can also be iterated

mystr = "SilambarasanTR"
for i in mystr:
    print(i)