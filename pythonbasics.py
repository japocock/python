"""This is a 
multiline docstring."""

#Comments

print("Hello, World!")
if 5 > 2:
  print("Five is greater than two!")

#Variables do not need to be declared with any particular type and can even change type after they have been set.
x = 4 # x is of type int
x = "String" # x is now of type str
print(x)
#A variable name must start with a letter or the underscore character
#A variable name cannot start with a number
#A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
#Variable names are case-sensitive (age, Age and AGE are three different variables)

#Combine variables

x = 5
y = 10
z = x + y
print(x + y)
print(z)

#Variables of numeric types are created when you assign a value to them:
#There are three numeric types in Python:
#int
#float - Float can also be scientific numbers with an "e" to indicate the power of 10 e.g 35e3
#complex
x = 1    # int
y = 2.8  # float
z = 1j   # complex

#To verify the type of any object in Python, use the type() function:
print(type(x))

