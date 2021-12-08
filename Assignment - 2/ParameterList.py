#How to get list of parameters name from a function in Python?
import inspect
print("\nName: Siddhanth Jagtap")
def myfunc(a, b):
	return a**b
print()
print(inspect.signature(myfunc))
print()