#Python – Sum of tuple elements
def myfunc():
    print("\nName: Siddhanth Jagtap")
    T1 = tuple((7, 8, 9, 1, 10, 7))
    print("\nThe Original Tuple is : " + str(T1))
    r = sum(list(T1))
    print("\nThe Summation of Tuple Elements are : " + str(r))
    print()
myfunc()