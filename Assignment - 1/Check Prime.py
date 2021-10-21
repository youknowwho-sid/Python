#Program to check if a number is prime or not
def myfunc():
    print ("Name: Siddhanth Jagtap")
    i=int(1)
    c=int(0)
    x = int(input("Enter Number to check if prime or not: "))
    while (i<x):
        if(x%i==0):
            c += 1
        i += 1
    if (c==1):
        print (x,"is a Prime number")
    else:
        print (x,"is not a Prime number")
myfunc()