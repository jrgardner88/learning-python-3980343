# LinkedIn Learning Python course by Joe Marini
# Example file for working with functions


# define a basic function
def hello_func():
  print("hello world!")
  name = input("What is your name? ")
  print("Nice to meet you,", name)

hello_func()

# function that takes parameters
def hello_func(greeting):
  print("hello world!")
  name = input("What is your name? ")
  print(greeting, name)

hello_func("How's it going")
hello_func("What's up")

# function that returns a value
def cube(x):
  return x*x*x

result = cube(2)
print(result)

# function with default value for an parameter
def hello_func(greeting, name=None):
  print("hello world!")
  if name == None:
    name = input("What is your name? ")
  print(greeting, name)

hello_func(name="Billy", greeting="Nice to meet you")
# function with variable number of parameters
def multi_add(start, *args):
  result = start
  for x in args:
    result = result + x
  return result

print(multi_add(0, 4, 5, 10, 4, 10))