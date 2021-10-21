#Program to print Letter Pattern
def myfunc():
    print("Name: Siddhanth Jagtap")
    i = int(1)
    while(i<=5):
        j = int(1)
        while(j<=i):
            print(chr(i+64),end = "\t")
            j = j + 1
        print("\n")
        i = i + 1
myfunc()            