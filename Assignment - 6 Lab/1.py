#Name: Siddhanth Nilesh Jagtap Regno.: 21BCE7490    
def myfunc():
    l1 = list()
    l2 = list()    
    nl = list()

    print("Enter Natural numbers only for elements in List 1. (Any other number to exit List 1)") #accepting list 1
    while(True):
        x = int(input("Input: "))
        if(x>0):
            l1.append(x)
        else:
            break
    print("Enter Natural numbers only for elements in List 2. (Any other number to exit List 2)") #accepting list 2
    while(True):
        x = int(input("Input: "))
        if(x>0):
            l2.append(x)
        else:
            break
    for a in l1:                                                #traversing through first list
        if a not in l2:
            nl.append(a)
    for a in l2:                                                #traversing through second list
        if a not in l1:
            nl.append(a)
    print("All Unique Elements from both lists: ",nl)
myfunc()