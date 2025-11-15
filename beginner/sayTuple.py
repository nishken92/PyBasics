import numpy






# TUPLES

thistuple = ("apple","orange","banana")

x = (1,3,5,7)
y = list(x)
print(y)
z = [4,4,4]
for i in z:
    y.append(i)
print(y)

x = tuple(y)
print(x)

# If tuple created with only one element, then it requires a comma at the end.

a = (1,2,3,4,5)
(p,q,r,s,t) = a
print(p)
print(r)

a = (1,2,3,4,5)
(p,q,r,*s) = a
print(p)
print(r)
print(s)


"""
Tuple values can be assigned to variables in a single line.
This is called unpacking of tuple. 
If an asterik is added to one of the variable, it will add the elements of the tuple as a list to that variable,
till the number of remaining variables and number of remaining tuple elements become equal
"""

fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
(a,*b,c) = fruits
print(a)
print(b)
print(c)

for i in fruits:
    print("I am referring fruits tuple")

for i in range(len(fruits)):
    print(fruits[i])


i = 0
while i < len(fruits):
    print(fruits[i])
    print("iterated")
    i += 1

# Tuple values can be multipled within the same tuple by * like a numerical value

z = (1,2,3,4)
mul = z * 10
print(mul)

print(z.index(4))

setA = {1,2,1}
print(setA)