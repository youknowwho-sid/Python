#Program to Find Minimum of Two Numbers in a List
def myfunc():
    print("\nName: Siddhanth Jagtap")
    List1 = list()
    i=0
    while(i<2):
        k=i+1
        List1.append(input("\nEnter Element "+str(k)+" Of List: "))
        i=i+1
    print("\nMinimum in the List= ",min(List1))    
myfunc()