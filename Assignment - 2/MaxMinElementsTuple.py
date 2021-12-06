#Maximum and Minimum K elements in Tuple
def myfunc():
    print("\nName: Siddhanth Jagtap")
    T1 = tuple((5, 20, 3, 7, 6, 8))
    print("\nThe Original Tuple is : " + str(T1))
    k = int(input("\nEnter Number of Max and Min Elements to View: "))
    if(k < len(T1)):    
        T1 = list(T1)
        temp = sorted(T1)
        r = tuple(temp[:k] + temp[-k:])
        print("\nThe extracted values : " + str(r))
        print()
    else:
        print("\nInvalid Input")
myfunc()