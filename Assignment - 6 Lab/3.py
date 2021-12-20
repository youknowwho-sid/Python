#Name: Siddhanth Nilesh Jagtap Regno.: 21BCE7490    
def myfunc():
    x = int(input("Enter lower limit: "))       #accepting lower limit
    y = int(input("Enter upper limit: "))       #accepting upper limit
    mx = max(x,y)                               
    mn = min(x,y)                               
    LT = list()                                 #list to hold the elements in the range
    i = mn+1
    while i < mx:
        if(i%2 == 1):
            LT.append(i)
        i += 1
    LT.sort(reverse=True)                       #sorting the list in descending order
    print("LT =",LT)
myfunc()