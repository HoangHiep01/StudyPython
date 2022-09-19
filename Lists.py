# List: ordered, mutable, allows duplicate, elements

# Declare
example1 = ["a","b","c"]
example2 = list("abc") # trick division string into char
print(example1, example2, sep="\n")

# List string
strlist = ["1", "2", "3", "A", "B", "C", "C"]
print (strlist)

# List number
numlist = [0, 3, 2, 6, 4.5, -7, 6, -3.14]
print (numlist)

# Diff datatypes in list
mylist = ["It's", True, "that list can contain more than", 1, "datatype"]
print (mylist)

# Access an element
print (strlist[0]) # print 1
print (strlist[1]) # print 2
print (strlist[2]) # print 3
print (strlist[-1])# print C
print (strlist[-2])# print C
print (strlist[-3])# print B

for num in numlist:
	print (num, end=" ")
print()

# Check list
if "list" in mylist:
	print ("yes")
else:
	print ("no")

# Common methods

# len() return how many elements inside list
print (len(mylist))
print (len(example1))

# append(object) Append object to the end of the list
example1.append("Cat")
print(example1)
example1.append("Dog")
print (example1)

# insert(index, object) Insert object before index
print("insert")
example1.insert(0,"Fish")
print (example1)
example1.insert(2, "Bird")
print (example1)

# pop() Remove and return last element
eledrop = example1.pop()
print (example1, eledrop,  sep="\n")

# remove(value) Remove first exist inside list
# Raises ValueError if the value is not present

print (numlist)
eledrop = numlist.remove(6)
print (numlist, eledrop,  sep="\n")

# clear() remove all elements from list

print (example1)
example1.clear()
print (example1)

# reverse() Reverse "IN PLACE"

print (mylist)
mylist.reverse()
print (mylist)

# softed() ascending order set as default

example2 = sorted(numlist)
print (numlist, example2, sep="\n")

# soft() ascending order set as default

print (numlist)
numlist.sort()
print (numlist)

# Trick

# Create new a list with the same element multiple times

times = 5
newlist = [0] * times
print (newlist)

# incorporate list

newlist = strlist + numlist
print (newlist)

# Slicing list

print (numlist)
print (numlist[2:5]) # print from index 2 to 4
print (numlist[:5])  # print from beginning index to 4
print (numlist[2:])  # print from index 2 to the end
print (numlist[::2]) # print from beginning to the end with step is 2 (default is 1)
print (numlist[::-1])# print from the end to beginning, nice trick to reverse

# Copying list using .copy() method
# If we declare orglist and wrote cpylist = orglist
# That's mean the both list refer to the same list inside memory
# What's happened with cpylist, orglist is too

mylist = numlist.copy()
# also use:
# mylist = list(numlist)
# mylist = numlist[:]
print (mylist) 

# List comprehension

squarelist = [num*num for num in numlist]
print (squarelist)