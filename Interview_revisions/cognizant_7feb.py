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

# Dictionary elements are accessible by key names

