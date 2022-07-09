# Functions in python are the first object class
# So, like other object
# They can be defined inside another function
# Passed as an argument to another function
# And even return from another function

# Concept
# Take other function as an argument
# Extend it without modify
# 
# @mydecorator
# def dosomthing():
# 	pass
# 	
# dosomething() would be extended with the functionality of this mydecorator

# Example
def start_end_decorator(func):	# take function as an argument

	def wrapper():	# define another function inside function
		print("Start")
		func()
		print("End")

	return wrapper	# return function inside function

def hello():
	print("Hello")

hello = start_end_decorator(hello)
hello()

# Also we can do

@start_end_decorator
def hi():
	print("Hi")

hi()

# When function take some argument, we will get error if we do like example
# So, ...
def improvedecorator(func):

	def wrapper(*args, **kwargs):
		print("Start")
		func(*args, **kwargs)
		print("End")
	return wrapper

@improvedecorator
def good9(obj):
	print(f"Good night, {obj}")

good9("Earth")

# We still have a problem, it's return value
# You can try return a value and it will print None if do the same above
# So, 
def improvedecorator2(func):

	def wrapper(*args, **kwargs):
		print("Previous extended")
		result = func(*args, **kwargs)
		print("Next extended")
		return result

	return wrapper

# use improvedecorator and improvedecorator2 to see different
@improvedecorator2
def Ilove(obj):
	print("Do something")
	return f"I luv {obj}"

print(Ilove("Autumn"))

# Last issue with decorator is information about function
print(help(Ilove))
print(Ilove.__name__)
# to fix this, we use functools
# Finally, we got a template

import functools

def mydecoderator(func):

	@functools.wraps(func)
	def wrapper(*args, **kwargs):
		# Do something
		result = func(*args, **kwargs)
		# Do something
		return result

	return wrapper

# Also decorator function can take another arguments, not only func
# So, ...

def repeat(num_times):
	def decorator_repeat(func):
		@functools.wraps(func)
		def wrapper(*agrs, **kwargs):
			for _ in range(num_times):
				result = func(*agrs, **kwargs)
			return result

		return wrapper

	return decorator_repeat

@repeat(num_times=3)
def greet(name):
	print(f"Hello {name}")

def greet2():
	print("Not expend by decorator func")

greet("World")
greet2()
# Now, I hate coding
# We can use multiple decorators by stack it above
# On top do first and next

# DECORATOR CLASS

class CountCalls:

	def __init__(self, func=None):
		self.func = func
		self.numcalls = 0

	def __call__(self, *agrs, **kwargs):
		self.numcalls += 1
		print(f"This is executed {self.numcalls} times")
		return self.func(*agrs, **kwargs)

@CountCalls
def sayhello():
	print("Hello")

for _ in range(3):
	sayhello()