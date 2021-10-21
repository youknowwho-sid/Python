#Program to display Fibonacci series using While - Loop
def myfunc():
    print ("Name: Siddhanth Jagtap")
    n = int(input("Enter the number of terms: "))
    a = int(0)
    b = int(1)
    print (a)
    print (b)
    i = int(3)                                          #since 2 terms are already printed, counter 'i' is set to 3
    while (i<=n):
        c = a + b
        print (c)
        a = b
        b = c
        i = i + 1
myfunc()