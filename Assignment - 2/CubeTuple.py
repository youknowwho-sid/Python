#Create a list of tuples from given list having number and its cube in each tuple
def myfunc(L1):
    print("\nName: Siddhanth Jagtap")
    r = [(val, pow(val, 3)) for val in L1]    
    print("\n"+str(r))
    print()
L = [1, 2, 3, 5]
myfunc(L)