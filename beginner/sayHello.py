if(1 > 2):
    print("Five is greater than two");
    print("hello nisanth");
else:
    print("Not so great");

x = 20;
y = 10;
z = x + y;
print(z);

#this is a comment nobody cares

"""
This is also a comment that nobody cares, but me !!
"""

"""
No separate variable declaration. 
If the variable is reassigned with values of different data types, 
the auto assignments will also take place without giving any error.
"""

x = 4       # x is of type int
print(f"Type of the variable X is , {type(x)}");
x = "Sally" # x is now of type str
print(x)

"""
String variables can be declared using single or double quotes.
variables are case sensitive
"""

"""
Variables can be assigned values in the below ways too
"""
x = y = z = 45;
print(x);
print(y);
print(z);

a, b, c = 10, "Hello Ken", "#$@#$#"
print(a);
print(b);
print(c);


#Unpacking of variables from a collection

fruitsAndNumbers = ["Mango", 5, "Banana"];
x,y,z = fruitsAndNumbers;
print(x);
print(y);
print(z);


x = "Py"
y = "is"
z = "awesome"
print(x+y+z);

#Output using Print statements

x = "Py"
y = "awsome"
print(x + y);

x = 10
y = 10
print(x + y);

#Example of Global and Local Variables
x = "Awsome"

def function():
    print("Py is " + x);
    y = "tester"

function();
print(y);

#Example for Global keyword
x = "Awsome"

def function():
    print("Py is " + x);
    global y 
    y = "tester"

function();
print(y);



r = range(1,5);
print(list(r));


b = bytes([67,6]);
print(b);

x = float(2);
print(x);

x = str(45);
print(x);


#Assigning multi line strings to variable

a = """vanakkam,
this is a multi string
thank you"""

print(a[4:11]);

print(a[:10]);

print(a[11:]);

b = "Hello, World!"
print(b[-5:-2]);

"""
In a string, if you count the index left to right it is positive indexing. 
If you count from right to left, it is negative indexing.
"""

b = " Hello, World! "
print(b.upper());
print(b.lower());
print(b.strip());
print(b.replace("H","J"));
print(b.split(" "));

#F-String is introduced in py 3.6 used for formatting

iVersion = 12;
x = f"I Phone version is {iVersion}";
print(x);
x = f"I Phone version is {iVersion + 2}";
print(x);
x = f"I Phone version is {5 + 2}";
print(x);
price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)

print(f"{10:^10}");
print("\f");
print("\165");



#String Methods

x = "guiltfree"
print(x.capitalize());

x = "GUILTFREE"
print(x.casefold());

x = "GUILTFREE"
y = "I AM ABOUT TO DEVELOP TO TO"
z = "AS HOBBY PROJECT"
print(x.center(40));
print(y.center(40));
print(z.center(40));
print(y.count("TO"));

x = "Anil";
print(x.endswith("l"));


txt = "H\te\tl\tl\to"

print(txt);
print(txt.expandtabs());
print(txt.expandtabs(2));
print(txt.expandtabs(4));
print(txt.expandtabs(10));

txt = "Dude movie releasing this Diwali Diwali Diwali"
print(txt.find(""));

# Format map funtion replaces the variables to the placeholders in a string.
# the value can be taken from a dictionary

details = {"name":"Nolan", "age": 55}
wishes = "Happy Birthday {name} ! Your age is {age} !!"
print(wishes.format_map(details));

# index and find funtion both returns index of the string only,
# however, find returns -1 and index returs error if string not found

txt = "T0feaf!555வணக்கம்"
print(txt.isascii());

a = "\u0030" #unicode for 0
b = "\u0047" #unicode for G

print(a.isdecimal())
print(b.isdecimal())

# Identifier is a word that can be used to name variable or funtion in a programming language

a = "0rt"
print("string a is Identifier : ",a.isidentifier());

b = "10.45"
print(b.isdigit());
print(b.isnumeric());

# isnumeric() and isdigit() performs the same function, but isnumberic extends for unicode characters too

c = "   e ";
print(c.isspace());

d = "Hello, This can be given as a title"
e = "Hello, This Can Be Given As A Title"

print("This is a Title: ", d.istitle());
print("This is a Title: ", e.istitle());

x = {"name" : "Nolan", "age" : 55, "job" : "director"};
print(", ".join(x));

y = "   Don"
z = y.lstrip();
print("SRK acted in ", z);
print("SRK acted in ", y);


txt = "Hello Sam!"
mytable = str.maketrans("S", "P")
print(mytable);

print(txt.translate(mytable));

x = "Road Side Shops are Side of the road"
print(x.partition("Side"));
print(x.rpartition("Side"));
print(x.partition("Are"));

print(x.replace("Side", "Front"));

print(x.rindex("t"));

x = "Hey, Mister, Where are you looking";
print(x.split(","));

y = """kokki pottu than
sikka vechitta
sokki thavikiren
baby"""

print(y.splitlines());

z = "MANNAN naan"

print(z.swapcase());

a = "jane"
print(a.zfill(11));

a = 0
print(bool(a));

x = 300;
print(isinstance(x, float));

d = 14 % 3;
print(d);

e = 2**4
print(e)


#Floor division rounds the value to nearest whole number

f = 30 // 6
print(f)


x = 5;
x += 5;
print(x)
x -= 5;
print(x)
x *= 5
print(x)
x /= 5
print(x)
x //= 2
print(x)

y = 12
y %= 5
print(y)

y **= 4
print(y)

if 5 != 5:
    print("eq")
else:
    print("ne")

print(not(5 > 7 or 5 > 2))

x = "Hello"
y = "Hello00"

print("In operator check")
print(y in x)

"""
In python, a number or expression is considered truthy or falsy based on boolean expression.
for example zero is false. 
"""

print(1 and [])