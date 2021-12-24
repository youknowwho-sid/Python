#Name: Siddhanth Nilesh Jagtap Regno.: 21BCE7490
#Program to find x ^ y using recursion

def power(a,b):
    if(b==1):
        return a
    else:
        return a * power(a,b-1)             #recursive function to calculate power


def myfunc():                           #main function
    x = int(input("Enter base: "))              #taking input values
    y = int(input("Enter power: "))
    print("Output:", power(x,y))            #calling the recursive function
myfunc()