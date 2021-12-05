#Ways to remove ith character from string in Python
def myfunc():
    print("\nName: Siddhanth Jagtap")
    s1 = input("\nEnter String: ")
    s2 = ""
    c = int(input("\nEnter index of character to be removed: "))
    
    s3 = ""    
    for i in range(len(s1)):
        if i != c:
            s3 = s3 + s1[i]
    
    print("\nString After Removal of Character at Index "+str(c)+":",s3)
    
    s4 = s1[:c] + s1[c+1:]
    print("\nString After Removal of Character at Index "+str(c)+" Using String Slicing:",s4)
    print()
myfunc()