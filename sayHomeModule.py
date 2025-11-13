
import sayModules as sm
import platform

# If a file is saved with .py extension, it is considered as module.
# The funtions in that module can be used by other python files through function calls
# Syntax is module_name.function(parameters)
# Module should be first imported
# modules can be renamed with 'as' keyword


sm.sayHello("Nisanth")

# Like methods in modiles, the data in the mdoule can also be reused.

print(sm.friend["name"])

x = platform.processor()
print(x)

# dir() is a built in funtion that lists all methods in a module

x = dir(sm)
print(x)

# Only parts of modules can be imported using 'from' keyword
# Once after the part is imported, do not use the module name while using that method or attribute