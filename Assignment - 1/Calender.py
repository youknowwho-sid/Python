#Program to Print a Calender, Taking Input From User, Using a Loop
def myfunc():
    print ("Name: Siddhanth Jagtap")
    x = int(input("Enter Number of Days in Month: "))
    y = int(input("Enter Day to Start From: 0 - Sunday, 1 - Monday ... 6 - Saturday: "))
    dt = int(1)
    if(y>6 or y<0):
        print ("Invalid Input")
    else:
        print ("SUN\t\tMON\t\tTUE\t\tWED\t\tTHU\t\tFRI\t\tSAT\n\n")
        sp = int(0)
        while (sp<y):
            print("\t\t",end = "")
            sp = sp + 1
        while (dt <= x):
            if (y != 0):
                if (y % 7 == 0):
                    print ("\n")
            print (dt,end ="\t\t")
            dt = dt + 1
            y = y + 1
myfunc()