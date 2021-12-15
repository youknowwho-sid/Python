#Name: Siddhanth Nilesh Jagtap Regno: 21bce7490
def myfunc():
    s = 0
    i = 7
    while(i<=7490):             #iterating numbers from 7 to 7490
        j = 1
        f = 1
        while(j<=i):            #while loop to calculate the factorial of every number between 7 to 7490
            f *= j              #f stores the factorial
            j += 1
        s += f                  #s stores the sum of all factorials
        i += 1
    print("\nSum=",s)
myfunc()