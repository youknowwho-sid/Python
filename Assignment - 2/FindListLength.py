#Program to Find Length of a List
def myfunc(List1):
    print("Name: Siddhanth Jagtap")
    len1 = len(List1)
    len2 = 0
    for i in List1:
        len2+=1
    print("Length Using len()=",len1)
    print("Length Using Counter=",len2)
    
List1 = [1,3,5,7,9]
myfunc(List1)