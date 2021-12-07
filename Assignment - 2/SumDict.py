#Python program to find the sum of all items in a dictionary
def myfunc():
    print("\nName: Siddhanth Jagtap")
    myDict = {'a': 100, 'b':200, 'c':300}
    list = []
    for i in myDict:
        list.append(myDict[i])
    final = sum(list)
    print()
    print("Sum: ",final)
    print()
myfunc()