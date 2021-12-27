#Name: Siddhanth Nilesh Jagtap Regno: 21BCE7490
#Python program to count lowercase character in a text file named Vit.txt

def myfunc():
    c = 0
    f = open("Vit.txt","r")             #open file
    data = f.read()                     #store data
    print("File Data=")
    print(data)
    print("\nNumber of lowercase characters=")
    l = data.replace(",","").replace(".","").replace(":","").split()
    for w in l:
        i = 0
        while(i<len(w)):
            if(w[i].islower() == True):
                c += 1                  #counter to count lowercase alpha
            i += 1
    print(c)
    f.close()

myfunc()