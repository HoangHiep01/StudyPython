# String: ordered, immutable, text representation

# Declare 
mytring1 = ""
mytring2 = ''


# If u want print a sentence contain ' like: I'm student
mytring1 = "I'm student"
mytring2 = 'I\'m student'

# Multiple line representation
mytring3 = """Hello
World"""
print(mytring3)

# Access string
# Can not be change value
mytring = "Hello World"
firstchar = mytring[0]
lastchar = mytring[-1]

# Slicing
# string[start:end:step]
substring = mytring[0:5] # Hello
print(substring)
substring = mytring[::-1] # nice trick reverse
print(substring)

# Concatenated string
greeting = "Hello"
obj = "visitors"
sentence = greeting + " " + obj
print(sentence)

# Use with loop
for char in mytring:
	print(char)

# Check string contain another string
mytring = "Hello World"
substring = "ello"
if substring in mytring:
	print("yes")
else:
	print("no")

# strip() remove whitespace
mytring = "    Hello   "
print(mytring)
mytring = mytring.strip() # Cuz immutable
print(mytring)

# upper() have all upper case
mytring = "hello"
print(mytring.upper())

# lower() have all lower case
mytring = "HeLlO"
print(mytring.lower())

# startswith() check string start with word or subtring
print(mytring.startswith("H"))
print(mytring.startswith(substring))

# endswith() check string end with word or subtring
print(mytring.endswith("O"))
print(mytring.endswith(substring))

# find() return first index of subtring in string
mytring = "Hello World"
print(mytring.find("o"))
print(mytring.find("ll"))

# count() return how many subtring inside string
print(mytring.count("Wor"))

# replace() return a copy that new substring replace old substring
print(mytring.replace("ll", "ILL"))

# split(sep, maxsplit)
# Return a list of the words in the string, using sep as the delimiter string
# sep: whitespace is the default value
# maxsplit maximum number of splits to do, default -1 means no limit
mylist = mytring.split()
print(mylist)

# join() concatenate any number of strings
# Inserted string between each give string
# Return a new string
# Nice trick convert list into string
# Use to copy string
newstring = " ".join(mylist)
print(newstring)

# Format string
# %s string, %d int, %.f float
var = "string"
mytring = "Variable contain %s" % var
print(mytring)

var = 21.165545
var2 = "string"
mytring = "Variable contain {:.2f} and {}".format(var,var2)
print(mytring)

# highly recommended
var = 27.6515
mytring = f"Variable contain {var}"
print(mytring)