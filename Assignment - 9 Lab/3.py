#Name: Siddhanth Nilesh Jagtap Regno: 21BCE7490
#Python program to read the content of a file named abc.txt. Reverse the letters of each word. Write the content to a new file named vit.txt


def revv(str1):
    L1 = str1.split()                           #storing words in a list
    str2 = ""                                   #empty list for output
    L2 = list()
    for w in L1:
        w1 = ""
        i = len(w)-1
        while(i>-1):
            w1 = w1 + w[i]                      #making reverse of word
            i -= 1
        L2.append(w1)
    for w in L2:
        str2 = str2 + " " + w                   #concatinating reverse of all words
    return(str2.strip())                             

def myfunc():
    f = open("abc.txt","r")             #open file
    data = f.read()                     #store data
    print("File Data=")
    print(data)
    s2 = revv(data)
    f.close()

    g = open("vit.txt","w")
    g.write(s2)
    g.close()
    
    print("New file data: ")
    i = open("vit.txt","r")
    print(i.read())
myfunc()