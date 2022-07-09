"""
- The difference between arguments and parameters
- Positional and keyword arguments
- Default arguments
- Variable-length argument (*args and **kwargs)
- Container unpacking into function arguments
- Local vs. global arguments
- parameter passing (by value or by reference?)
"""

def printname(name):	# name use as parameter (tham số)
	print(name)

printname("Noname")	# "Noname" use as argument



def printnum(a, b, c, default = 4):
	print(a, b, c, default)

printnum(1,2,3)	# without keyword
# also
printnum(a=1, b=2, c=3)	# with keyword
# also
printnum(c=3, a=1, b=2)	# and with ketword, position is no matter
# still print 1 2 3 4 and work well with 3 argments
printnum(1,2,3,5)	# default changed
# Careful with syntax error



def printvar1(a, b, *args, **kwargs):
	
	print("a, b", (a,b))

	print("args")
	for arg in args:
		print(arg)

	print("kwargs")
	for key in kwargs:
		print(key, kwargs[key])

# *args used to pass any number of positional argument to ur func (tuple)
# **kwargs used to pass any number of keyword argument to ur func (dict)
# it's no matter *args, **kwargs. The important is * and **
# So, you can ...

def printvar2(a, b, *myconfig, **mysetup):
	
	print("a, b", (a,b))

	print("args as myconfig")
	for arg in myconfig:
		print(arg)

	print("kwargs as mysetup")
	for key in mysetup:
		print(key, mysetup[key])

printvar1(1,2, 3,4,5, num1=6,num2=7)
printvar2(1,2, 3,4,5, num1=6,num2=7)
# We have same result
# We also dont need them
printvar1(1,2, 3,4,5)
printvar1(1,2, num1=6,num2=7)
printvar1(1,2)

# when we define
# def foo(a,b, *, c,d):, after * are keyword args
# So, we must call foo(1,2,c=3,d=4)
# Same foo(*args, last): we must call foo(1,2,3, last=4)
# Because * will take all args and we must determine what last take



# Unpacking by use * and **
# Required length match with number of parameters
mylist = [1,2,3]
mytuple = (1,2,3)
mydict = {"a": 1, "b": 2, "c": 3}
print(*mylist)	# it print 1 2 3 not [1,2,3] like print(mylist)
print(*mytuple)	# also 1 2 3 not (1,2,3)
printnum(**mydict)	# Required length and key match with number and name of parameters and 



# If u want modify global var, u must declare
def modifyglobalvar():

	global number	# without this, number var below mean: create a local var name number equal 3
	x = number
	number = 3
	print(x)

number = 0
modifyglobalvar()
print(number)



# parameter passed in reference to an object
# but reference is passed by value
# mutable object can be changed within a METHOD
# Carefull cuz u change reference
# immutable cant be changed but can be reassigned if it contained within mutable object