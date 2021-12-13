'''Program to write the following code by taking n as user input
n = 5
A
AB
ABC
ABCD
ABCDE'''
def myfunc():
    n = int(input("Enter a Number: "))
    i = int(1)
    while(i<=n):
        j = int(1)
        while(j<=i):
            print(chr(j+64),end = "")
            j = j + 1
        print()
        i = i + 1
myfunc()    