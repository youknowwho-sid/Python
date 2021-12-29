#Name: Siddhanth Nilesh Jagtap Regno.: 21BCE7490
#Program for recursive function that calculate sum of first n natural numbers. 

def sum(n):
    if (n==0):
        return 0
    else:
        return n + sum(n-1)             #sum by recursion

def myfunc():
    x = int(input("Enter a number: "))                  #accept input
    res = sum(x)                    #call function
    print(res)
myfunc()