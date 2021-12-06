#Python program to print even length words in a string
def myfunc():	
    print("\nName: Siddhanth Jagtap")
    s1 = input("\nEnter a String: ")
    s1 = s1.split(" ")  
    for w in s1:
        if(len(w)%2 == 0):
            print("\n"+w)
    print()
myfunc()