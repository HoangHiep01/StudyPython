# Dictionary: key-value pairs, unordered, mutable

# Declare
mydict = {"animal": "Dog", "age": 2, "color": "black"}
print(mydict)

mydict2 = dict(animal="Cat", age=1.5, color="white")
print(mydict2)

# Access by key not index
# Wrong key will raise KeyError
print(mydict["animal"], mydict["age"], mydict["color"], sep="\n")

# Add and change value

print(mydict)
mydict["status"] = "normal"
print(mydict)
mydict["status"] = "sick"
print(mydict)

# Delete value

del mydict["status"]
mydict.pop("age")
mydict.popitem() # remove last item since python 3.7
print(mydict)

# Check value

if "age" in mydict2:
	print(mydict2["age"])
else:
	print("have no key")

if "ability" in mydict2:
	print(mydict2["ability"])
else:
	print("have no key")

try:
	print(mydict2["animal"])
	print(mydict2["ability"])
except:
	print("Catch error when meet it")

# Use with loop

for key in mydict2:
	print(key)
for key in mydict2.keys():
	print(key)
for value in mydict2.values():
	print(value)
for key, value in mydict2.items():
	print(key, value)

# Copy dictionary
# Do not use cpydict = mydict
# Same List.py, Both dict point to the same dict inside memory
# That's mean we work with same dict but use another name
# Make actual copy
# There are 2 ways

cpydict = mydict2.copy()
cpydict = dict(mydict2)

# Merge dict

mydict["status"] = "normal"
print (mydict, mydict2, "merge", sep="\n")
mydict.update(mydict2)
print (mydict)

# Use tuple as a key, cuz tuple can be change, it the same key in dict
# Can not do it with list

mytuple = (2,4)
mydict3 = {mytuple: "Even"}

print (mydict3[mytuple])