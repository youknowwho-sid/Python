#Program to check if a number is Palindrome or not using While - Loop
def myfunc():
    print ("Name: Siddhanth Jagtap")
    x = int(input("Enter a Number: "))
    s = int(0)
    t = x
    while(t!=0):
        r = t % 10
        s = s * 10 + r
        t = t // 10
    if (s==x):
        print (x,"is a Palindrome number")
    else:
       print (x,"is not a Palindrome number")
myfunc()