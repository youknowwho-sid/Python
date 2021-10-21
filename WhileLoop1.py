#To Use While Loop To Print The Numbers Between Two Inputs Accepted From User
def myfunc():
    x = (int(input("Enter a number = ")))
    y = (int(input("Enter a number = ")))
    if x > y:
        max = x
        min = y
    else:
        max = y
        min = x
    i = min
    while (i <= max):
        print (i)
        i=i+1
myfunc()