import json

#Though it is named as jsonobj, it is a dict object
jsonobj = {
    "name" : "Nisanth",
    "age" : 33
}


# dumps method converts the data type into json format
# JSON formats are strings

converted = json.dumps(jsonobj)
print(converted)
print(type(converted))
print(type(jsonobj))

a = "x"
print(a)
convertedX = json.dumps(a)
print(convertedX)

x = 12
print(json.dumps(x))
y = json.dumps(x)

# Below two commented lines will give an error because "y" is not an integer.
# Since "y" converted to json format through dumps method, it is a string now
#z = 15 + y
#print(z)
p = x + 15
print(p)


# loads() method

k = "10"
print(type(k)) # This is a str, which is in json format

l = json.loads(k)
print(type(l)) # Here the type is int, because the string is converted to python data type using loads() method

print(json.dumps(True))

# A none python obkect will be conveted to null obkect in json format


fruits = ["banana"]
fruitjson = json.dumps(fruits)
print(type(fruitjson))
print(fruitjson)