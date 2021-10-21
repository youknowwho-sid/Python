#Program To Accept And Calculate The Average Of 5 Subject Exam Scores
def myfunc():
    x1= int(input("Enter marks in subject 1: "))
    x2= int(input("Enter marks in subject 2: "))
    x3= int(input("Enter marks in subject 3: "))
    x4= int(input("Enter marks in subject 4: "))
    x5= int(input("Enter marks in subject 5: "))
    s= float(x1+x2+x3+x4+x5)/5
    print (s)
myfunc()