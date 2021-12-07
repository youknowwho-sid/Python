#Python program to find the size of a Tuple
import sys
def myfunc():
    print("\nName: Siddhanth Jagtap")
    T1 = ("V", "I", "T", "A", "P")
    print("\nLength of Tuple: " + str(len(T1)))
    print("\nSize of Tuple: " + str(sys.getsizeof(T1)) + " bytes")
    print()
myfunc()