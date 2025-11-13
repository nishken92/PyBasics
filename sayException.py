# EXCEPTIONS
"""
try block performs the action
except block catches if there is an error. Otherwise it will not run
else block will run if no error generated
finally will run regardless of error generation
"""
#Exception prevents a program from crashing after an error occurred

try:
    print(x)
except:
    print("An error occurred")
else:
    print("Program executed successfully")
finally:
    print("Testing the finally statement")


x = "hello"

if not type(x) is int:
  raise TypeError("Only integers are allowed")