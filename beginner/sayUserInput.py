"""
Python stops executing when it sees and input() method. It starts the execution again once 
the input is received
"""
print("What is your name ?")
name = input()
print("Hello", f"{name}." " Good Day !")


# Input("Prompt"), once this is executed, the prompt will appear in the screen.
# There is no need of print statement

input("Done")
print("You entered control C right ?")

# Multiple input functions can be introduced in the program.
# Python will stop executing each time the input statement is appearing

a = input("Enter a Number")
b = float(a)
print(b + 5)

#It is always a good practice to validate the input received from user

x = input("Enter a number")
try:
    y = float(x)
except:
    print("Not a number")
else:
    print("Entered a number")
finally:
    print("Check Done")