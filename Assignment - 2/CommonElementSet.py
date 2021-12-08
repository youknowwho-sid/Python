#Python – Check if two lists have atleast one element common
print("\nName: Siddhanth Jagtap")
def myfunc(a,b):
    print("\nSet 1: " + str(a))
    print("\nSet 2: " + str(b))
    print("\nCommon elements exist: ",end="")
    if len(a.intersection(b)) > 0:
        print(True)
    else:
        print(False)
    print()

x = set(([1, 2, 3]))
y = set(([1, 3, 5]))
myfunc(x,y)

c = set((["a", "b", "c"]))
d = set((["d", "e", "f"]))
myfunc(c,d)