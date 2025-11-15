"""
IF CONDITIONS
"""
# If condition with multiple statements

a = 10
b = 15
if a > b:
    print("A is greater than B")
else:
    print("B is greater than A")
    print("This is to test multiple statements")

# If condition comparing boolean

c = []
if c:
    print("C is not an empty collection")
else:
    print("C is empty")

d = None
if d:
    print("D is NOT NONE")
else:
    print("D is NONE")

e = False
if e:
    print("E is TRUE")
else:
    print("E is FLASE")

f = -2
if f:
    print("F is NON ZERO")
else:
    print("F is ZERO")

"""
Elif: this is used when multiple true statement needs to be checked

"""

mark = 40
if mark >= 81:
    print("First class")
elif mark >= 61 and mark <= 80:
    print("Second class")
elif mark >=41 and mark <=60:
    print("Third class")
else:
    print("Fail")

# Shorthand if

# Syntax 
# if condition: operation

if 10 > 5: print("Ten is greater than Five")

# Syntax of shorthand if else
# expression 1 if condition else expression 2

a = 45
b = 35
print("A is greater than B") if a > b else print("B is greater than A")

# values can be assigned using shorthand if else. 
# Note that the assignment operator is used only once

x = 2
y = 4

bigger = x if x > y else y 

print("Bigger Number is:" ,bigger)

p = 10
q = 12

# Multiple if else statements can be chained
# Syntax
# expression1 if condition1 else expression2 if condition2 else expression3 if condition3

print("P is greater than Q") if p > q else print("Both are equal") if p == q else print("Q is greater than P")


"""
Logical Operators : These are used to combile conditional operators
and
or
not
"""

tier1 = ["Rajinikanth",2]
tier2 = ["Dhanush",3]
tier3 = ["Harish Kalyan",10]

print(tier1[0])

if tier3[1] > tier2[1]:
    if tier2[1] > tier1[1]:
        print(tier1[0]," is the biggest actor")
    else:
        print(tier2[0]," is the biggest actor")
else:
    print(tier1[0], " is the biggest actor")



x = 71

if x > 50:
    print("X is greater than Fifty")
    if x > 70:
        print("X is greater than 70 also")
else:
    print("X is less than 50")

# PASS Statements
# Pass is a null operator
# If the expression following an if statement has nothing to do, a pass can be inserted
# This will prevent from any syntax errors
# pass is not comment, python will execute it

a = 10
b = 15
if b > a:
    pass

    
