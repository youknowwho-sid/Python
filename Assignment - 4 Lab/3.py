#Name: Siddhanth Nilesh Jagtap Regno: 21bce7490
def myfunc():
    c = 0                                                       #setting the counter
    z = 7490                                                    #defining loop control variable
    while(z!=0):
        r = z%10                                                #extracting digits
        if(r==0):
            c += 1
        z //= 10
    print("\nNumber of occurences of 0 in 7490:",c)
myfunc()