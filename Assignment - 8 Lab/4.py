#Name: Siddhanth Nilesh Jagtap Regno.: 21BCE7490
#Python program to enter a string and reverse the words of the string

def myfunc():
    str1 = input("Enter a String: ")            #taking input
    L1 = str1.split()                           #storing words in a list
    str2 = ""                                   #empty list for output
    L2 = list()
    for w in L1:
        w1 = ""
        i = len(w)-1
        while(i>-1):
            w1 = w1 + w[i]                      #making reverse of word
            i -= 1
        L2.append(w1)
    for w in L2:
        str2 = str2 + " " + w                   #concatinating reverse of all words
    print(str2.strip())                         #printing output with strip method to eliminate leading or trailing spaces
myfunc()    