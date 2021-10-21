#Program to find GCD of two numbers using For - Loop
def myfunc():
    print ("Name: Siddhanth Jagtap")
    x = int(input("Enter First Number: "))
    y = int(input("Enter Second Number: "))
    if (x > y):
        big = x
        small = y
    else:
        big = y
        small = x
    for k in range(big):
        l = k+1
        if (small % l == 0 and big % l ==0):
            gcd = l
    print ("GCD of the Entered Numbers is =",gcd)
myfunc()    