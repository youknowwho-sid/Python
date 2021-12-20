#Name: Siddhanth Nilesh Jagtap Regno.: 21BCE7490    
def myfunc():
    D = {}
    c = 'Y'
    while(c=='Y' or c=='y'):
        k = input("Enter Key: ")                                #accepting dictionary from user
        v = input("Enter Value: ")
        D[k] = v
        c = input("Enter Y to add another input. Enter any other key to exit.\n")    
    print("Original Dictionary:",D) 
    inp = input("Enter key: ")
    if inp in D.keys():
        k = 0                                                   #setting flag
    else:
        k = 1
    if(k==0):
        print("Value =",D[inp])                                 #if found printing value
    else:
        v = input("Enter Value: ")          
        D[inp] = v                                              #adding key and value if not found
        print("Updated Dictionary:",D)       
myfunc()    