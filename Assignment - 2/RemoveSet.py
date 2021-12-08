#Python – Remove items from Set
def myfunc():
    print("\nName: Siddhanth Jagtap")
    S = set([1,2,3,4,5,6,7,8,9,10])
    T = set(S)
    print("\nOriginal Set: " + str(S))
    for i in T:
        if (i>5):
            S.remove(i)
    print("\nSet After Removing Elements: "+str(S))
    print()
myfunc()