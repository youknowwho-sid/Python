#Name: Siddhanth Nilesh Jagtap Regno.: 21BCE7490    
def myfunc():
    OL = list()   
    NL = list()
    print("Enter List Elements: (any letter to exit)")
    while(True):
        ch = input()
        if(ch.isalpha()==False):
            inp = int(ch)
            OL.append(inp)
        else:
            break
    print("OL: ",OL) 
    i = 0       
    s = 0
    while(i<len(OL)):
        if(OL[i]%2 == 0):
            NL.append(OL[i])
            s += OL[i]
        i += 1
    print("NL: ",NL)
    M = s/len(NL)
    print("M =",M)
myfunc()