#Name: Siddhanth Nilesh Jagtap Regno.: 21BCE7490
#Python program to define a function which takes a string argument and returns a dictionary containing characters and their frequency

def myfunc():
    str1 = input("Enter a string: ")        #taking input
    f = {}                                  #dictionary to store characters with their frequency
    for x in str1:
        if x in f:
            f[x] += 1
        else:
            f[x] = 1
    print("Dictionary of characters with their frequency:")
    print(f)                                #printing the dict
myfunc()