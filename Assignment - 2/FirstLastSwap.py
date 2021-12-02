#Program to Interchange First and Last List Elements
def myfunc(List1):
    print("Name: Siddhanth Jagtap")
    print("\nList: ", List1)
    length = len(List1)
    #Swap first element with last element using temporary variable
    t = List1[0]
    List1[0] = List1[length -1]
    List1[length-1] = t
    print("\nList After Interchanging First and Last List Elements", List1)

List1=[1,3,5,7,9]
myfunc(List1)