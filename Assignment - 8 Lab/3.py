#Name: Siddhanth Nilesh Jagtap Regno.: 21BCE7490
#Program to Check Whether a String is Palindrome

def myfunc():
    str1 = input("\nEnter String: ")            #take input
    length = len(str1)
    i = length - 1
    str2=""
    while (i>-1):
        str2 =  str2 + str1[i]              #creating reverse string
        i = i - 1   
    if str1 == str2:                        #checking if forward and reverse strings are equal
        print("\nString is Palindrome")
    else:
        print("\nString is Not Palindrome")
    print()
myfunc()