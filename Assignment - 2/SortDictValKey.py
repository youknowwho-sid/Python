#Python | Sort Python Dictionaries by Key or Value
def myfunc():
    print("\nName: Siddhanth Jagtap")
    D1 = {"o":3, "j":4, "e":5, "v":2, "a":1}
    t=[]

    for key,value in sorted(D1.items()):
        t.append((key,value))
    print(f"\nDictionary Sorted by Keys: {dict(t)}")

    print(f"\nDictionary Sorted by Values: {dict(sorted(D1.items(), key = val_Sort))}")
    print()

def val_Sort(e):
    return e[1]

myfunc()