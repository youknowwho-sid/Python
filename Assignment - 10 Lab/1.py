#Name: Siddhanth Nilesh Jagtap Regno.: 21BCE7490
#Program that reads two integers from keyboard and calculate the greatest common divisor (gcd) using recursive function.

def gcd(a,b):
    if(b==0):   
        return a                        #base case
    else:
        return gcd(b,a%b)
def myfunc():
    a=int(input("Enter first number: "))
    b=int(input("Enter second number: "))                   #accept inputs
    GCD=gcd(a,b)                    #call function
    print("GCD is: ")
    print(GCD)
myfunc()