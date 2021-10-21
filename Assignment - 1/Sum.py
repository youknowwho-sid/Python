#Program to find the sum of natural numbers using While - Loop
def myfunc():
    print ("Name: Siddhanth Jagtap")
    x = int(input("Enter the upper limit for sum calculation: "))
    i = int(1)
    s=0
    while (i<=x):
        s += i
        i = i + 1
    print ("Sum of first",x,"natural numbers = ",s)
myfunc()