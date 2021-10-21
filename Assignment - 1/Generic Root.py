#Program to Print the Generic Root of a Number Using While - Loop
def myfunc():
    print ("Name: Siddhanth Jagtap")
    x = int(input("Enter a Number: "))
    s = int(0)
    while (True):
        r = x % 10
        s = s + r
        x = x // 10
        if (x==0):
            x = s
            s = 0
            if(x<10):
                break
    print ("Generic Root =",x)
myfunc()