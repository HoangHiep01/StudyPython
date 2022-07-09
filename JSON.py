import json

person = {"name": "John", "age": 30, "city": "NewYork", "hasChildren": False, "title": ["engineer", "programmer",]}

# Convert to string
personJSON = json.dumps(person, indent=4)

print(personJSON)

# Write a json file
with open("person.json", "w") as file:
	json.dump(person, file, indent= 4)

# Convert to py dict
personConvertBack = json.loads(personJSON)
print(personConvertBack)

# Convert from file to py dict
with open("example.json", "r") as file:
	personConvertBack = json.load(file)
	print(personConvertBack)

# encode class to json
# use default argument

class User:

	def __init__(self, name, age):
		self.name = name
		self.age = age

user = User("Max", 27)

# Convert in4 to dict handle otherwise handle error
def encodeuser(obj):
	if isinstance(obj, User):
		return {"name": obj.name, "age": obj.age, obj.__class__.__name__: True}
	else:
		raise TypeError("Object not type User is not JSON serializable")

useJSON = json.dumps(user, default=encodeuser, indent=4)
print(useJSON)

# Second way
from json import JSONEncoder

class UserEncoder(JSONEncoder):

	def default(self, obj):
		if isinstance(obj, User):
			return {"name": obj.name, "age": obj.age, obj.__class__.__name__: True}
		return JSONEncoder.default(self, obj)

useJSON2 = UserEncoder(indent=4).encode(user)
print(useJSON2)

# decode json to class
# use object_hook argument

def decodeuser(dict):
	if User.__name__ in dict:
		return User(name=dict["name"], age=dict["age"])
	return dict

user = json.loads(useJSON, object_hook=decodeuser)
print(user.name, user.age, type(user))