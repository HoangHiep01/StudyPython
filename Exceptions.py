# Errors and Exceptions
x = -5

if x <= 0:
	raise Exception("x should be positive.")

# also

# if not true, raise assert error
assert (x > 0), "x should be positive."

# handle

try:
	a = int("t")

except Exception as err:
	print(err)
except:
	print("Unknown Error happened")

# also

try:
	a = 5 / 0
	b = a + "0"
except ZeroDivisionError as zde:
	print(zde)
except TypeError as te:
	print(te)
except:
	print("Unknown Error happened")
else:
	print("Have no error catched")
finally:
	print("Always run.")

# Build own exception

class ValueTooHighError(Exception):
	pass

class ValueTooSmallError(Exception):
	def __init__(self, message, value):
		self.message = message
		self.value = value

def testvalue(x):
	if x > 100:
		raise ValueTooHighError("value too high")
	if x < 5:
		raise ValueTooSmallError("value too small", x)

try:
	testvalue(1)
except ValueTooHighError as err:
	print(err)
except ValueTooSmallError as err:
	print(err.message, err.value)