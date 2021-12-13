'''Writting the above program with the starting letter as first letter of your name.(suppose the 
name starts with letter x) If the letter reaches Z it should start from A again.
For example
 X
 X&Y
 X&Y&Z
 X&Y&Z&A
X&Y&Z&A&B'''
def myfunc():
    n = int(input("Enter a Number: "))
    i = int(1)
    k = int(1)
    sp = 20
    while(i<=n):
        while(k<sp):
            print(" ",end="")
            k += 1
        j = int(1)
        l = int(19)             #19 is the value for S
        while(j<=i):
            if(l+64<91):
                if(j!=i):
                    print(chr(l+64),end = "&")
                else:
                    print(chr(l+64),end = "")
                j = j + 1
                l = l + 1
            else:
                if(j!=i):
                    print(chr(l+64-26),end = "&")
                else:
                    print(chr(l+64-26),end = "")
                j = j + 1
                l = l + 1
        print()
        i = i + 1
        k = 1
        sp -= 1
myfunc()  