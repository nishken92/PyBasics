#SET

# Once set is created, the elements cannot be changed, but elements can be added and removed

a = {1,2,3,4}

for i in a:
    print(i)

# discard and remove perform same funtion. However, if the item to be removed is not present in the 
# set, then remove will return an error but discard will not.

a = {1,2,3,4,5,6}
x = a.pop()
print("popped out item is ")
print(x)

x = {1,2,3,4,5}
y = {4,5,6,7,8}

z = y.symmetric_difference(x)
print(z)

k = {10,20,30,40,50,60,70}
h = {40,45,50,55,60,65,70,75,80,85,90,95,100}

j = k.symmetric_difference(h)
print(j)

# STRING JOIN

"""
The update() method and union() methods joins two sets and ignore the duplicates
intersection() method keeps only the duplicates
difference() method keeps the elements from first set which is not present in the second
symmatric_difference() keeps elemets which are not duplicate
"""

# Froze sets are immutable sets

x = frozenset({1,2,3})
print(type(x))

k = {40,50,60,70}
l = frozenset(k)
print(type(k))
print(type(l))

m = {40,45,50,55,60,65,70,75,80,85,90,95,100}
n = frozenset(m)

print(n.issuperset(l))


p = {1,2,3,4}
q = {4,5}
p.difference_update(q)
print(p)
p.discard(3)
print(p)
p.discard(1)
print(p)

p = {1,2,3,4,5}
q = {5,6,7,8}

p.intersection_update(q)
print(p)
