import math

# Math module has methods to perform mathematical tasks

# min() and max() methods returns the minimum and maximum value in an iterable

iterable = range(10,100,10)
for i in iterable:
    print(i)
print(iterable)

x = min(iterable)
y = max(iterable)

print(x)
print(y)

# abs() returns the absolute value of given number

x = abs(-7.25)

print(x)

# pow() returns the power
# syntax - pow(x,y)

print(pow(2,5))

x = math.sqrt(79)
print(x)

# The ceil() and floor() methods in math module will round off the float number to
# upper and lower integer number

a = 1.2
print(math.ceil(a))
print(math.floor(a))

