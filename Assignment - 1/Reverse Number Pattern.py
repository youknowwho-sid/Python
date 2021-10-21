#Program to print Reverse Star(*) Program
def myfunc():
    print("Name: Siddhanth Jagtap")
    i = int(5)
    while(i>=1):
        j = int(1)
        while(j<=i):
            print(j,end = "\t")
            j = j + 1
        print("\n")
        i = i - 1
myfunc()   