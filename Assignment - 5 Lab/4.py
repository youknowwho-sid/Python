#Name: Siddhanth Nilesh Jagtap Regno: 21bce7490
def myfunc():
    n = 20                                  #7+4+9+0 = 20
    i = 1
    sum = 0
    while(i<=n):
        j = 1
        fact = 1                            #calcuting factorial
        while(j<=i):
            fact *= j
            j += 1
        sum += i/fact                       #calculating sum
        i += 1
    print("Sum =",sum)
myfunc()  