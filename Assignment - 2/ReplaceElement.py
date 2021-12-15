#Replace NumPy array elements that doesn’t satisfy the given condition
import numpy as np
def myfunc(): 
    c = 5
    print("\nName: Siddhanth Jagtap")
    arr = np.random.randint(1,10,(3,3))
    print(f"Original array: \n\n {arr}")
    arr[arr > c] = 50
    print(f"\nElements that are greater than 5 are replaced with 50: \n\n {arr}")
    arr[arr < c] = -50
    print(f"\nElements that are lesser than 5 are replaced with -50: \n\n {arr}")
    print()
myfunc()