#To Work A Basic Program On If-Elif-Else
def myfunc():
    x = (int(input('Enter Marks out of 100 = ')))
    k=1
    grade = ""
    if(x>=90 and x<100):
        grade = 'A'
    elif(x>=80 and x<90):
        grade = 'B'
    elif(x>=70 and x<80):
        grade = 'C'
    elif(x>=60 and x<70):
        grade = 'D'
    elif(x>=50 and x<60):
        grade = 'E'
    elif(x>=0 and x<50):
        grade = 'F'
    else:
        print("Invalid Input")
        k=0
    if(k==1):
        print ("Grade = " + grade)
myfunc()