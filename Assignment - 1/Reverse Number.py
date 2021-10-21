#Reverse a given number using While - Loop
def myfunc():
    print ("Name: Siddhanth Jagtap")
    x = int(input("Enter a number: "))
    s=int(0)
    while(x!=0):
        r = x % 10
        s = s * 10 + r
        x = x // 10
    print ("The Reversed Number Is: ",s)
myfunc()