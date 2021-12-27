#Name: Siddhanth Nilesh Jagtap Regno: 21BCE7490
#Create a file named vitstudent.txt. In each line the file will have [regno, name, specialization, contact no]. 
#Write the data for 10 students to the file. Write a Python code to search and display details of student whose regno is Y.

def myfunc():
    Y = "21BCE7490"                 #regno

    with open("vitstudent.txt", "r") as f:          #open file
        for l in f.readlines():
            det = l.replace("["," ").replace("]", " ").replace("\n", " ").split(",")
            if (det[0].strip() == Y):                   #check for regno
                print(det)                              #print data for that student
myfunc()