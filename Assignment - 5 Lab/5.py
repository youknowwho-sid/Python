#Name: Siddhanth Nilesh Jagtap Regno: 21bce7490
def myfunc():
    y = 7**4                                 #7**4 because y = A^B as per qsn
    i = 1 
    sum = 0
    while(i<=y):
        if(i%2 == 0):
            sum -= 1/i                      #subtracting if denominator is even
        else:
            sum += 1/i                      #adding if denominator is odd
        i += 1
    print("Sum =",sum)
myfunc()