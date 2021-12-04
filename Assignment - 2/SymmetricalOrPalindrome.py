#Program to Check Whether a String is Symmetrical or Palindrome
def myfunc():
    print("\nName: Siddhanth Jagtap")
    str1 = input("\nEnter String: ")

    length = len(str1)
    if (length % 2 == 0):
        s1 = str1[:(length//2)]
        s2 = str1[(length//2):]
        if s1 == s2:
            print("\nString is Symmetrical")
        else:
            print("\nString is Not Symmetrical")
    else:
        s1 = str1[:(length//2)]
        s2 = str1[((length//2) + 1):]
        if s1 == s2:
            print("\nString is Symmetrical")
        else:
            print("\nString is Not Symmetrical")    
            
    i = length - 1
    str2=""
    while (i>-1):
        str2 =  str2 + str1[i] 
        i = i - 1
    if str1 == str2:
        print("\nString is Palindrome")
    else:
        print("\nString is Not Palindrome")
    print()
myfunc()