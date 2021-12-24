#Name: Siddhanth Nilesh Jagtap Regno.: 21BCE7490
#Python program to enter a string and find the character that has highest frequency

def myfunc():
    str1 = input("Enter a string: ")        #taking input
    f = {}                                  #dictionary to store characters with their frequency
    for x in str1:
        if x in f:
            f[x] += 1
        else:
            f[x] = 1
    o = max(f, key = f.get)                  #finding out the max from all dict values
    print ("Character that has highest frequency: '" + str(o)+"'")              #printing output
myfunc()