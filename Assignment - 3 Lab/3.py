'''Write a program to print the pattern if n = 5, n may be any positive number. 
 A
 A&B
 A&B&C
 A&B&C&D
 A&B&C&D&E'''
def myfunc():
    n = int(input("Enter a Number: "))
    i = int(1)
    k = int(1)
    sp = 20
    while(i<=n):
        while(k<sp):
            print(" ",end="")
            k += 1
        j = int(1)
        while(j<=i):
            if(j!=i):
                print(chr(j+64),end = "&")
            else:
                print(chr(j+64),end = "")
            j = j + 1
        print()
        i = i + 1
        k = 1
        sp -= 1
myfunc()  