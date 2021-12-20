#Name: Siddhanth Nilesh Jagtap Regno.: 21BCE7490    
def myfunc():
    S = input("Enter a string: ")
    FL = S.split(" ")    #creating list of separated words
    print(FL)
    NL = FL
    i = 0
    VD = {}             #vowel dictionary
    CD = {}             #consonant dictionary
    while (i<len(FL)):  
        c = 0
        w = FL[i]
        for w1 in NL:                   
            if w1 == w:     
                c += 1                  #counting frequency
        if(w[0] == 'a' or w[0] == 'e' or w[0] == 'i' or w[0] == 'o' or w[0] == 'A' or w[0] == 'E' or w[0] == 'I' or w[0] == 'O' or w[0] == 'U' or w[0] == 'u'):
            VD[w] = c                   #checking if vowel
        else:
            CD[w] = c
        i += 1
    print("VD: ",VD)
    print("CD: ",CD)
myfunc()