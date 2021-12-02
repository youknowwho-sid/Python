#Python Program to Swap 2 Elements in a List
def myfunc(List1,i,j):
    print('Name: Siddhanth Jagtap')
    print("\nList = ", List1)
    a = List1[i]
    List1[i] = List1[j]
    List1[j] = a
    print("\nList After Swapping = ", List1)

List1 = [1,3,5,7,9]
i = 1
j = 3
myfunc(List1,i,j)