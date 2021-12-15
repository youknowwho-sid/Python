#Name: Siddhanth Nilesh Jagtap Regno: 21bce7490
def myfunc():
    c = 0                                                       #setting the counter
    z = 7490                                                    #defining loop control variable
    while(z!=0):
        r = z%10                                                #extracting digits
        if(r%9==0):                                             #checking if digit is divisible by 9
            c += 1
        z //= 10
    print("\nNumber of digits divisible by 9 in 7490:",c)
myfunc()