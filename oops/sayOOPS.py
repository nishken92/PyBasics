# OBJECT ORIENTED PROGRAMMING

"""
Oops gives better organization and resuability

"""

# Scope test

def func():
    def do_local():
        spam = "NIS"
        print("Print statement from the innermost scope: ", spam)
        return spam
    def do_nonlocal():
        nonlocal spam
        spam = "NISHAN"
        print("This is from innermost scope but variable declared as non local: ",spam)
    def do_global():
        global spam
        spam = "NISHANTH KENNATH"
        return spam
    spam = "N"
    print("Value of the spam initially inside func(): ", spam)
    do_local()
    print("Checks if the value goes back to N even after local func returns", spam)
    do_nonlocal()
    print("Checks if the value not going back to N:", spam)
    do_global()
    print("Make sure now it is global:",spam)

func()
print("Make sure now it is global:",spam)



class MyClass:
    """Docuemtnation testing"""
    j = 15
    i = 10

print(MyClass.__doc__)