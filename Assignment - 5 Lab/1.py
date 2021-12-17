#Name: Siddhanth Nilesh Jagtap Regno: 21bce7490
#Program to convert registration number to binary, octal and hexadecimal
def binary(a):
    b = 0                           #binary variable
    c = 0                           #counter
    t = a                        #temp variable to hold input
    while(t > 0):
        b += ((t%2)*(10**c))
        t //= 2
        c += 1
    print("Binary =",b)
    print()
binary(7490)

def octal(a):
    o = 0                           #octal variable
    c = 0                           #counter
    t = a                        #temp variable to hold input
    while(t > 0):
        o += ((t%8)*(10**c))       
        t //= 8
        c += 1
    print("Octal =",o)
octal(7490)

def hex(a):
    i = 0
    hd = []                         #making list to store alphanumeric data
    while a!=0:
        r = a % 16
        if r<10:
            r = r+48                #storing int as per ascii
        else:
            r = r+55                #storing string as per ascii
        r = chr(r)
        hd.insert(i, r)
        i += 1
        a //= 16

    print("\nHexadecimal = ",end="")
    i -= 1
    while i>=0:
        print(end=hd[i])
        i -= 1
    print()
hex(7490)