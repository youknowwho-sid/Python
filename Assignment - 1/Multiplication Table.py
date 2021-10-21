#Program to print multiplication table using For - Loop
def myfunc():
    print ("Name: Siddhanth Jagtap")
    x = int(input("Enter number to print multiplication table: "))
    for i in range(10):
        j=i+1
        print(x,"x",j,"=",(x*j))
myfunc()