'''Write a program to initialize two integer variables with the first and last character of your 
name in small letter. convert the characters in your name to ASCII code. Find the nth prime 
number in the range. Where n is the last digit of your registration number. Do not write any 
generalised program, instead write the specific program, where all the inputs except the last 
digit of the registration number are fixed.
OUTPUT:
First character of my name: A :65
Last character of my name :Z :90
The last digit of my registration number: 3
The 3rd prime number in the range is: 73'''
def myfunc():
    l1 = ord('s')
    l2 = ord('h')
    print("\nGiven range = ",min(l1,l2),"to",max(l1,l2))
    t1 = l1
    t2 = l2
    c = 0
    flag = 0
    print("\nTo find the 9th prime number in the range, since last digit of reg. no = 0 and second last digit = 9")
    #finding 9th prime number in the given range
    while(t2<t1):
        k = 0
        cf = 0
        for div in range(1,t2):                 #loop to check prime
            if(t2 % div == 0):
                cf = cf + 1
            if (cf>2):
                k=1
                break
        if(k==1):
            pass
        else:
            c += 1        
        if(c==9):                           #validity of code can be checked by changing c==9 to any value less than 3
            flag = 1
            break
        t2 += 1
    if(flag == 1):
        print("Output: ",t2)  
    else:
        print("\nOut of range, there are only",c,"prime numbers in the given range")
    print()
myfunc()