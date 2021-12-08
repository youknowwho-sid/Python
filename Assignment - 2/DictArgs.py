# Functions that accept variable length key value pair as arguments
def myfunc(**args):
    print("\nName: Siddhanth Jagtap")
    print()
    return args

print(myfunc(A=65, B=66, C=77))
print()