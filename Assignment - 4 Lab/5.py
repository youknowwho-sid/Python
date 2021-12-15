#Name: Siddhanth Nilesh Jagtap Regno: 21bce7490
def myfunc():
    s = 0
    b = False                           
    c = 0
    z = 7490
    while(b == False):                              #setting a flag to terminate loop
        while(z!=0):                                #calculating sum of digits
            r = z % 10
            s += r
            c += 1
            z //= 10
        if(s<10):                                   #changing flag value if s is single digit
            b = True
        else:
            z = s                                   #re-assigning z as s and continuing the operation
            s = 0                                   
    print("\nSum =",s)
    print("\nNumber of Operations =",c)
    print()
myfunc()