# How to use *

# multiple
print(3*2)

# power operation
print(3**2)

# create list with n element number
# Also work with tuple, str
n = 5
zeros = [0] * n
print(zeros)

# Take arguments and Unpacking see more details in Func.py, and some trick unpacking in I learn datatype
# recommended that u should watch vid, src in README.md

# Merge

mylist = [1,2,3]
mytuple = (4,5,6)
myset = {7,8,9}
mergelist = [*mylist, *mytuple, *myset]
print(mergelist)

dic1 = {"a":1, "b":2}
dic2 = {"c":3, "d":4}
mergedict = {**dic1, **dic2}
print(mergedict)