#Name: Siddhanth Nilesh Jagtap Regno: 21bce7490
#Add function
def add(A,B):
    if(B>1):
        sum = (add(add(A,B-1),1))
        if (sum!=None):
            print("Sum =",sum)
    else:
        i = 1
        s = 0
        if (A!= None):
            while(i<=A):
                s = s+i
                i += 1
            return(s)
a = 7
b = 4
add(a,b)