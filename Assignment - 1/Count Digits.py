#Program to Count the Number of Digits in a Number Using While - Loop
def myfunc():
    print ("Name: Siddhanth Jagtap")
    x = int(input("Enter a Number: "))
    t = x
    c = int(0)
    while(t!=0):
        r = t % 10
        c = c + 1
        t = t // 10
    print ("The number of digits in",x,"=",c)
myfunc()