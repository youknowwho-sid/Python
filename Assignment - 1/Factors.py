#Program to Print Factors of a Number
def myfunc():
    print ("Name: Siddhanth Jagtap")
    x = int(input("Enter A Number: "))
    print("It's factors are: ")
    i = int(1)
    while (i<=x):
        if (x % i == 0):
            print (i)
        i = i + 1
myfunc()