# Tuple: ordered, immutable, allows duplicate elements

# Declare
mytuple = ()
mytuple = tuple() # can have an argument, if not, return empty tuple
numtuple = (0,3,2)
strtuple = ("Cat", "Dog","Frog")
mytuple = (0, "Cat", True)
print (mytuple, numtuple, strtuple)

is_not_tuple = ("element")
is_tuple1 = ("element1",)
is_tuple1 = "element1", "element2", "element3"

# Access an element
# Same list
item = numtuple[0]
print (item)

# Can not be change value
# numtuple[0] = 7 wll raise TypeError

# Check element

if "Tiger" in strtuple:
	print ("yes")
else:
	print ("no")

# Common Methods
mytuple = ("a", "p", "p", "l", "e")

# len() return number of items a container
print (len(mytuple))

# count() return number of specific items a container
print (mytuple.count("p"), mytuple.count("b"))

# index() return first index of specific items, if have no item, raise ValueError

print (mytuple.index("a"), mytuple.index("p"))

# Convert list to tuple and tuple to list

mylist = list(mytuple)
mytuple2 = tuple(mylist)

print (type(mylist), type(mytuple2))

# Slicing tuple using colon
# Same list
mytuple = (1,2,3,4,5,6,7,8,9,10)
print (mytuple[2:5])
print (mytuple[2:])
print (mytuple[:5])
print (mytuple[::2])
print (mytuple[::-1])

# Unpacking
# The number of elemeny must match with the element inside tuple
mytuple = "Cat", 2, "Gray"
name, age, color = mytuple
print (name, age, color, sep="\n")
# Unpack multiple element with *

mytuple = (1,2,3,4,5)

i1, *i2, i3 = mytuple
print (i1, i2, i3, sep="\n")

# Compare list and tuple

from sys import getsizeof

mylist = [0,1,2, "hello", True]
mytuple = (0,1,2, "hello", True)
print (getsizeof(mylist), "bytes")
print (getsizeof(mytuple), "bytes")
# list use more memory than tuple

from timeit import timeit
print (timeit(stmt="[0,1,2,3,4,5]", number=10**6))
print (timeit(stmt="(0,1,2,3,4,5)", number=10**6))
# list need more time to create than tuple
# 
# efficient when work with large data