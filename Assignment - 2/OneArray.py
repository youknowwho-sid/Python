#Create a Numpy array filled with all ones
import numpy as np
def myfunc():
    print("\nName: Siddhanth Jagtap")
    arr = np.ones([2,2], dtype=int)
    print(F"\nOnes Matrix created using .ones() method: \n\n {arr}")

    brr = np.full([2,2], 1)
    print(f"\nOnes Matrix using .full() method: \n\n {brr}")
    print()
myfunc()