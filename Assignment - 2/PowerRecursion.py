#Python program to find the power of a number using recursion
print("\nName: Siddhanth Jagtap")
def myfunc(n,p):
    if(p==0):
        return 1
    return n*myfunc(n,p-1)

num = int(input("\nEnter number: "))
pow = int(input("Enter power: "))
print()
print("Output: " + str(myfunc(num,pow)))
print()