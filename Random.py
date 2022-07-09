import random as rd

# default in range(0,1)
print(rd.random())

#  get random number in range [a,b) or [a,b] depending on rounding
print(rd.uniform(1,2.9))

# get random int number in range [a,b]
print(rd.randint(1,10))

# get random int number in range[a,b)
print(rd.randrange(1,10))

# have no idea
print(rd.normalvariate(0,1))

# get random element in list
mylist = list("ABCDEFGH")
print(rd.choice(mylist))

# get random elements in list, pick only one
num = 3
mylist = list("ABCDEFGH")
print(rd.sample(mylist, num))

# get random elements in list, pick multiple times
num = 3
mylist = list("ABCDEFGH")
print(rd.choices(mylist, k=num))

# shuffle list on place
rd.shuffle(mylist)
print(mylist)

# use seed() to reproduce number

rd.seed(1)
print(rd.random(), rd.randint(1,10))
rd.seed(2)
print(rd.random(), rd.randint(1,10))

rd.seed(1)
print(rd.random(), rd.randint(1,10))
rd.seed(2)
print(rd.random(), rd.randint(1,10))

# use lib: secrets
# security purposes
import secrets

# random number in range [0, n)
print(secrets.randbelow(10))

# random number with k bits
# if k = 4, we have 0000:0 to 1111:15
print(secrets.randbits(4))

# random pick
mylist = list("ABCDEFGH")
print(secrets.choice(mylist))

# use lib: numpy
import numpy as np

# random array with n float values in range(0,1)
n = 3
print(np.random.rand(n))
# or matrix same way
print(np.random.rand(n,n))

# random array with n int values in range[a,b]
print(np.random.randint(0,10,n))
# or matrix same way, use tuple
print(np.random.randint(0,10,(n,n)))

# shuffle value
arr = np.array([[1,2,3],[4,5,6],[7,8,9]])

print(arr)
np.random.shuffle(arr)
print(arr)

# seed method in numpy
# completely different seed in random module
# recomended that should use seed in numpy

np.random.seed(1)
print(np.random.rand(3,3))
np.random.seed(1)
print(np.random.rand(3,3))

# got the same arr in video, cuz of seed method ?