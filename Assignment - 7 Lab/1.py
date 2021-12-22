#Name: Siddhanth Nilesh Jagtap Regno.: 21BCE7490    
def myfunc():
    i = 0
    Name = list()
    Sub1 = list()
    Sub2 = list()
    Sub3 = list()
    Sub4 = list()
    Sub5 = list()
    Avg = list()
    
    while(i<10):                                     #taking all input
        s = 0
        nm = input("Enter Name of student "+str(i+1)+": ")
        Name.append(nm)
        m1 = int(input("Enter marks in subject 1: "))
        Sub1.append(m1)
        s += m1
        m2 = int(input("Enter marks in subject 2: "))
        Sub2.append(m2)
        s += m2
        m3 = int(input("Enter marks in subject 3: "))
        Sub3.append(m3)
        s += m3
        m4 = int(input("Enter marks in subject 4: "))
        Sub4.append(m4)
        s += m4
        m5 = int(input("Enter marks in subject 5: "))
        Sub5.append(m5)
        s += m5
        Avg.append(s/5)                             #calculating average
        i += 1
    print("\nStudents who failed:\n")
    j = 0
    while(j<10):
        if(Avg[j]<50):
            print(Name[j]+": "+str(Avg[j]))
        j += 1

myfunc()