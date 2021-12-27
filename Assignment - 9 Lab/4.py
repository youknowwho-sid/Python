#Name: Siddhanth Nilesh Jagtap Regno: 21BCE7490
#Python program to define a function that will read lines from a text file "vit.txt", and display all the words, 
#which are greater than N(0) characters

def myfunc():
    N = 0                               #last digit of regno
    f = open("Vit.txt","r")             #open file
    data = f.read()                     #store data
    print("File Data=")
    print(data)
    print("\nWords with length greater than 0 =")
    l = data.split()
    for w in l: 
        if(len(w)>N):                   #checking length
            print(w)
    f.close()

myfunc()