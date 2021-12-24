#Name: Siddhanth Nilesh Jagtap Regno.: 21BCE7490
# Python program to calculate the sum of a list of prime numbers from m to n using recursion

def recur_sum(m,n):
   if n <= m:
        if(ifPrime(n)==True):
            return n
        else:
            return 0
   else:
        if(ifPrime(n)==True):
            return n + recur_sum(m,n-1)             #recursion to find sum
        else:
            return 0 + recur_sum(m,n-1)

def ifPrime(p):
    i = 1                           #checking if number is prime
    c = 0
    while(i<p):
        if(p%i == 0):
            c+=1                #counter to count number of factors
        i+=1
    if(c == 1):
        return True
    else:
        return False

def myfunc():
    m = int(input("Enter lower limit: "))                       #taking input
    n = int(input("Enter upper limit: "))                       #main function
    m1 = min(m,n)
    m2 = max(m,n)
    print("Sum =",recur_sum(m1,m2))
myfunc()