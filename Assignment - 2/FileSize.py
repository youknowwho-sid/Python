#How to check file size in Python?
import sys
def myfunc():
    print("\nName: Siddhanth Jagtap")
    print("\nnew.txt is ", sys.getsizeof("new.txt"), "bytes")
    print("\ntext.txt is ", sys.getsizeof("text.txt"), "bytes")
    print()
myfunc()