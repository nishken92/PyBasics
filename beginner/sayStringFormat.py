import math

# F Strings are methods to format a string
# A normal string is a sequence of character inside quotes
# Meanwhile, F Strings are executables.


# Anything within the curly brackets of the the F string is considered as python code.
# It will be evaluated in real time

# The curly braces are placeholders which can contain variables, operators etc
name = "Nisanth"
age = 33
statement = f"Customer name is {name}, and age is {age}. Now I am going to perform a math {math.sqrt(16)}"
print(statement)

tax = 18
price = 1567
finalprice = f"The final price is {price + ((price/100)*18)}"
print(finalprice)

price = 51
print("price is ",f"{price} .", "It is", f"{'expensive' if price > 50 else 'moderate' }")

# Built in object methods can be executed within F Strings

fruit = "BaNaNa"
print(f"{fruit.lower()}")


# Formatting Types

print(f"Right Aligning {'these':>50} characters")
print("Here are the list of Film Makers and ther films")
mylist = [{
    "film" : "Vada Chennai",
    "Director" : "Vetrimaran"
},
{
    "film" : "Madras",
    "Director" : "Pa Ranjith"
}]

for i in mylist:
    print(i["film"], f"{'':^30}" ,f"{i["Director"]:<30}")

# to convert the number to unicode format format
print(f"{6773:c}")

# user comma as thousands separator
print(f"{10347623465:,}")

print(f"nishken ,{-5:=10}")

# to convert the number to binary format
print(f"{109348:b}")

