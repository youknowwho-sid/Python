#Create a Numpy array filled with all zeros
import numpy as np
def myfunc():
    print("\nName: Siddhanth Jagtap")
    arr = np.zeros([2,2], dtype=int)
    print(f"\nZero Matrix created by .zeros() method: \n\n {arr}")

    brr = np.full([2,2], 0)
    print(f"\nZero Matrix using .full() method: \n\n {brr}")
    print()
myfunc()