#How to read specific lines from a File in Python?
def myfunc():
    with open("anthem.txt", "r") as f:
        line = f.readlines()
    print("\nName: Siddhanth Jagtap")
    print(f"\nFirst line: {line[0]}")
    print(f"\nThird line: {line[2]}")
    print(f"\nFifth line: {line[4]}")
    print()
myfunc()