#Python – Row-wise element Addition in Tuple Matrix
def myfunc():
    print("\nName: Siddhanth Jagtap")
    T1 = tuple(([('ABC', 1), ('DEF', 1)], [('HIJ', 2)], [('KLM', 3), ('NOP', 3)]))
    el = tuple(([1,2,3]))
    print("\nFirst Tuple: ",T1)
    print("\nSecond Tuple: ",el)
    if (len(el)!=len(T1)):
        print("\nInvalid Input")        
    else:
        for i in range(len(T1)):
            n = 0
            for j in T1[i]:
                n+=1
            t = (el[i],)           
            for x in range (n):
                T1[i][x] = T1[i][x] + t   
        print()
        print(T1)
        print()
myfunc()