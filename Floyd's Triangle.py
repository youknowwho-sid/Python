def myfunc():
   number = 1
   for i in range(4):
        for j in range(1+i):
            print(number, end = " ")
            number += 1
        print()
myfunc()