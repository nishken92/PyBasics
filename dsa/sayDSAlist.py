# DATA STRUCTURES AND ALGORITHMS

# LISTS AND ARRAYS

# Lists act as a dynamic array. It is ordered, mutable and can contain data of different data types.

z = ["x",3.14,-89,("flower","tree"),{"movie":"Vadachennai","director":"Vetrimaran"},True]
print(z)

x = [60,40,30,100,120,45,35]
x.sort()
print(x)
x.append(95)
print(x)
x.sort()
print(x)

# Here the sort function makes change in the list object, but it returns none.

a = [9,2,3,4,5,6]

def minVal(testlist):
    x = testlist
    x.sort()
    return x[0]

value = minVal(a)
print("The lowest number of the array is:", value)