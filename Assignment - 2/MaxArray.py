#Get the max value from given matrix
import numpy as np
def myfunc():
    print("\nName: Siddhanth Jagtap")
    arr = np.random.randint(1,10,(3,4))
    print(f"Original Array: \n\n{arr}")

    max = float("-inf")
    for r in arr:
        for c in r:
            if c > max:
                max = c      
    print(f"\nMaximum element from the matrix is: {max}")
    print()
myfunc()