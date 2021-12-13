'''Program to write the following code by taking n as user input
n = 5
Ax
ABx
ABCx
ABCDx
ABCDEx, where x is last character of your name'''
def myfunc():
    n = int(input("Enter a Number: "))
    i = int(1)
    while(i<=n):
        j = int(1)
        while(j<=i):
            print(chr(j+64),end = "")
            j = j + 1
        print("H")
        i = i + 1
myfunc()    