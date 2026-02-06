a = ""
if a:
    print("nothing")
else:
    print("empty")

a = 10 if a else 20
print(a)
 # 20 will be the result

 # expression 1 if condirion 1 else expression 2 if condition2 else expression 3 if condition 3

b = 10
print("A is greater than B") if a > b else print("A and B are equal") if a == b else print("A is less than B")


tier1 = ["Rajinikanth",100]
tier2 = ["Ajith Kumar", 80]
tier3 = ["Sivakarthikeyan", 50]
tier4 = ["Harish Kalyan", 40]

grand_list = [tier1,tier2,tier3,tier4]
print(grand_list)

print(grand_list.sort())

from datetime import date, datetime
dt = datetime(2025,10,10,4,5,17)
print(dt)

# date time format puts a - between the units

# Dictionary is ordered , mutable and do not allow duplicates

dict1 = {
    "Name" : "Nisanth Kennath",
    "Age" : 33
}

print(dict1)
print(len(dict1))
print(dict1["Name"])

dict1.update({"Place" : "Chennai"})

dict1["Gender"] = "Male"

# Dictionary elements are accessible by key names

list1 = dict1.keys()
print(list1)
list2 = dict1.values()
print(list2)

dict1.pop("Gender")
print(dict1)


# popitem will delete the last item and return it back
print(dict1.popitem())
print(dict1)


dict1.clear()
print(dict1)


Movie = {
    "Name" : "Attakathi",
    "Year" : 2012,
    "Production" : "Thirukumaran Entertainment",
    "Director" : "Pa Ranjith",
    "Music" : "Santhosh Narayanan"
}

print(Movie)

# Dictionary is iterable over key
for i in Movie:
    print(i)

for i in Movie:
    print(Movie[i])

for i,j in Movie.items():
    print(i , ":", j)

# Copy is a method of the dict object meanwhile dict is an in-built function

Movie2 = Movie.copy()
print(Movie2)

Movie3 = dict(Movie2)
print(Movie3)

Movie4 = {
    "Bison": {
        "Director" : "Mari Selvaraj",
        "Year" : 2025
    },
    "Vadachennai" : {
        "Director" : "Vetrimaran",
        "Year" : 2018
    }
}
print(Movie4)

# Iterator is a countable list of numbers over which a loop can be iterated. 

ab = {1,2,3,4,5}
print(type(ab))
c = iter(ab)
print(type(c))
 # Any data type can be converted to an iterable using iter() and next()

try:
    print(next(c))
    print(next(c))
    print(next(c))
    print(next(c))
    print(next(c))
    print(next(c))
except:
    print("More items")
else:
    print("All good")
finally:
    print("I am finally")

# Characters in a string can also be iterated

name = "SILAMBARASAN TR"
for i in name:
    print(i)


import json

jsonobj = {
    "Name" : "Nisanth Kennath S",
    "Age" : 33
}

# dumps is the method to convert an object into JSON
# JSON objects are strings
# loads is the method that convert a string to corresponding data type

print(type(jsonobj))
converted = json.dumps(jsonobj)
print(type(converted))

h = "10"
k = json.loads(h)
print(type(k))


listing = ["Idukki", "Ernakulam"]
print(listing)
for i in listing:
    print(i)

listing.append("Thrissur")
print(listing)

print(len(listing))

# list() method is a constructor

district = list(("Coimbatore","Nilgiri"))
print(district)


# Negative indexing starts from the last item
print(listing[-2])



