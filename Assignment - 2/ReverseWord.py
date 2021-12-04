#Reverse Words in a Given String in Python
def myfunc():
    print("\nName: Siddhanth Jagtap")
    s1 = ' ' + input("\nEnter a String: ") + ' '
    s2=""
    l = len(s1)
    i = 0
    w=""
    while (i < l - 1):
        if (s1[i] == ' '):
            j = i+1
            while(s1[j] != ' '):
                w = w + s1[j] 
                j += 1
            i = j
            s2 = w + ' ' + s2
            w = ""
        else:
            i += 1
    s2.strip()
    print("\n"+s2)
    print()
myfunc()