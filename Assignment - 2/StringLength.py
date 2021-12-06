#Find length of a string in python (4 ways)
def fun1(s):
    l1 = len(s)   
    return l1 

def fun2(s):
    l2 = 0
    for i in s:
        l2 = l2 + 1
    return l2 

def fun3(s):
    l3 = 0
    while s[l3:]:
        l3 += 1
    return l3 


def fun4(s):    
    if not s:
        return 0
    else:
        temp = ""
        return ((temp).join(s)).count(temp) - 1

def main():
    print("\nName: Siddhanth Jagtap")
    s1 = input("\nEnter a String: ")
    print("\nLength of String Using len(): ",fun1(s1))
    print("\nLength of String Using For-Loop Iteration: ",fun2(s1))
    print("\nLength of String Using String SLicing",fun3(s1))
    print("\nLength of String Using join() and count(): ",fun4(s1))
    print()
main()