#Name: Siddhanth Nilesh Jagtap Regno: 21bce7490
#Print series
def myfunc():
    n = 1                           #we have to go till n = A + B = 7 + 4 = 11
    a = [1,]                        #making a list of all the an elements
    while(n<12):
        if(a[n-1] - n > 0): 
            a.append(a[n-1] - n)    #appending to the list
        else:
            a.append(a[n-1] + n)
        print(a[n-1])
        n += 1
myfunc()
