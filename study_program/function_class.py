import dis

def method():
	'''this function print and return my name'''
	name = "nick"
	print("l am", name)
	return name

print("help(method) : ")
print(str(help(method)) + "\n")

print("method.__doc__ : ")
print(method.__doc__ + "\n")

print("method.__name__ : ")
print(method.__name__ + "\n")

print("method.__code__ : ")
print(str(method.__code__) + "\n")

print("dis.show_code(method) : ")
print(str(dis.show_code(method)) + "\n")

class A(): pass

class Base(A):
	"""
	document there
	"""
	name="nick"
	__secret="123456"
	def __repr__():
		return name
	def say_hello(name):
		print("hello," + name)
	def _secret_method():
		return __secret__

Base.another="hello world"

print("Base.another : ")
print(Base.another + "\n")

print("Base.__doc__ : ")
print(Base.__doc__ + '\n')

print("Base.__module__ : ")
print(Base.__module__ + '\n')

print("Base.__class__ : ")
print(str(Base.__class__) + "\n")

print("Base.__dict__ : ")
print(str(Base.__dict__) + "\n")

print("Base.__bases__ : ")
print(Base.__bases__)
