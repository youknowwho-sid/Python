#Python dictionary with keys having multiple inputs
def myfunc():
    print("\nName: Siddhanth Jagtap")
    dict = {}
    x, y, z = 10, 20, 30
    dict[x, y, z] = x + y - z;
    x, y, z = 5, 2, 4
    dict[x, y, z] = x + y - z;
    print()
    print(dict)
    print()
myfunc()