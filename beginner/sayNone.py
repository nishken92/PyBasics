"""
None is an object of class Nonetype
"""

x = None
print(type(x))

# None evaluates to False in boolean context
print(bool(x))

# Below example shows that, if a project is not returing anything explicitly, it returns None by default

def myfunc():
    x = 5

y = myfunc()

print(y)