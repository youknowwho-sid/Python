#Name: Siddhanth Nilesh Jagtap Regno: 21bce7490
def myfunc():
    a = int(0)                                          #we start with 0 and 1 
    b = int(1)
    s = 1
    print (a)
    print (b)
    i = int(3)                                          #since 2 terms are already printed, counter 'i' is set to 3
    while (i<=4):                                       #going till the n'th value (according to question, n = 4)
        c = a + b
        s += c                                          #calculating sum
        print (c)
        a = b
        b = c
        i = i + 1
    print("\nSum:",s)
myfunc()