# Help save memory when work with large data
# It's look like

def mygenerator():
	print("Is it run when assign variable")
	yield 1
	yield 3
	yield 2

print(mygenerator())
for i in mygenerator():
	print(i)

# Also access
g = mygenerator()	# No, it's not
print(next(g))	# It's here
print(next(g))
print(next(g))
print(type(g))
# print(next(g)) will raise Error

# We can
print(sorted(mygenerator()))
print(sum(mygenerator()))

# See why said: save memory

from sys import getsizeof

def numgenerator(n):
	
	num = 0
	assert num < n,("Invalid value")
	while num < n:
		yield num
		num += 1

def numlist(n):
	assert n > 0, ("Invalid value")
	return [num for num in range(n)]

for i in numgenerator(15):
	print(i)

# a little bit diff
print(getsizeof(numgenerator(10)))
print(getsizeof(numlist(10)))
a1 = numgenerator(10**3)
a2 = numlist(10**3)
print(getsizeof(a1))
print(getsizeof(a2))

# let try bigger
print(getsizeof(numgenerator(10**6)))
print(getsizeof(numlist(10**6)))

# Used to finding fibo

def fibigenerator(limit):
	# 0, 1, 1, 2, 3, 5, 8, ...
	firstnum, nextnum = 0 ,1
	while firstnum < limit:
		yield firstnum
		firstnum, nextnum = nextnum, firstnum + nextnum

for i in fibigenerator(30):
	print(i)

# Also declare generator

mygenerator = (num for num in  range(10) if num % 2 == 0)
print(type(mygenerator))
# Don't confuse with
mylist = [num for num in  range(10) if num % 2 == 0]
print(type(mylist))