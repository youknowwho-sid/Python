#Name: Siddhanth Nilesh Jagtap Regno.: 21BCE7490
#Program for recursive function that accepts a decimal integer and display its binary equivalent

def binary(i,s):
    if (i == 0):
        return "0"+s
    else:
        r = i%2
        s = str(r) + s                      #create a binary string of the number
        return binary(i//2,s)


def myfunc():
    x = int(input("Enter a number: "))          #accept input
    res = binary(x,"")          #call function
    print(res)
myfunc()