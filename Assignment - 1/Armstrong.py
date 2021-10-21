#Program to check if a number is Armstrong Number or not using While - Loop
def myfunc():
    print ("Name: Siddhanth Jagtap")
    x = int(input("Enter A Number: "))
    s=0
    t=x
    while(t!=0):
        r = t % 10
        s += r*r*r
        t = t // 10
    if(s==x):
        print (x," is an Armstrong Number")
    else:
        print (x," is not an Armstrong Number")
myfunc()    