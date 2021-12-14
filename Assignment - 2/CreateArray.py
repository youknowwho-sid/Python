#How to create an empty and a full NumPy array?
import numpy as np
def myfunc():
    print("\nName: Siddhanth Jagtap")
    empty_arr = np.empty((2,2)) 
    print(f"Empty array: \n\n {empty_arr}")    
    full_arr = np.full((2,2), 1) 
    print(f"\nFull array: \n\n {full_arr}")
    print()
myfunc()