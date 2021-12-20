#Name: Siddhanth Nilesh Jagtap Regno.: 21BCE7490    
def myfunc():
    D = {}
    c = 'Y'
    k = 1
    while(c=='Y' or c=='y'):
        k = input("Enter Key: ")                                #accepting dictionary from user
        v = input("Enter Value: ")
        D[k] = v
        c = input("Enter Y to add another input. Enter any other key to exit.\n")       
    l = len(D)                                                  #finding length
    print("Original Dictionary:",D)
    print("Count:",l)
    inp = input("Enter key to delete: ")
    if inp in D.keys():
        k = 0                                                   #setting flag
    else:
        k = 1
    if(k==0):
        del D[inp]                                              #deleting input key if found
        print("After Deletion: ",D)
    else:
        print("Key Not Found")                                  #error message
myfunc()