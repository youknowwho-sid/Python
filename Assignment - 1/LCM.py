#Program to find LCM using While - Loop
def myfunc():
    print ("Name = Siddhanth Jagtap")
    x = int(input("Enter First Number: "))
    y = int(input("Enter Second Number: "))
    p = 1
    if (x > y):
        big = x
        small = y
    else:
        big = y
        small = x
    while (True):
        if (big % x == 0 and big % y == 0):
            print (big)
            break          
        big = big + 1
myfunc()